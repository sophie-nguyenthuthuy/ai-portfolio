-- =====================================================
-- ASSIGNMENT 3 - SECTION 3: SCHEMA NGÂN HÀNG
-- Câu 1: CREATE TABLE với khoá chính & khoá ngoại
-- =====================================================

DROP TABLE IF EXISTS giao_dich;
DROP TABLE IF EXISTS tai_khoan;
DROP TABLE IF EXISTS khach_hang;

-- Bảng KHÁCH HÀNG
CREATE TABLE khach_hang (
    ma_kh       INTEGER PRIMARY KEY,
    ho_ten      TEXT    NOT NULL,
    gioi_tinh   TEXT    CHECK (gioi_tinh IN ('Nam','Nữ')),
    ngay_sinh   DATE,
    tinh_thanh  TEXT    NOT NULL,
    ngay_mo_kh  DATE
);

-- Bảng TÀI KHOẢN (1 KH có nhiều TK)
CREATE TABLE tai_khoan (
    ma_tk       INTEGER PRIMARY KEY,
    ma_kh       INTEGER NOT NULL,
    loai_tk     TEXT    CHECK (loai_tk IN ('Thanh toán','Tiết kiệm')),
    so_du       REAL    NOT NULL DEFAULT 0,
    ngay_mo_tk  DATE,
    trang_thai  TEXT    DEFAULT 'Hoạt động',
    FOREIGN KEY (ma_kh) REFERENCES khach_hang(ma_kh)
);

-- Bảng GIAO DỊCH (1 TK có nhiều GD)
CREATE TABLE giao_dich (
    ma_gd       INTEGER PRIMARY KEY,
    ma_tk       INTEGER NOT NULL,
    loai_gd     TEXT    CHECK (loai_gd IN ('Nạp tiền','Rút tiền','Chuyển khoản')),
    so_tien     REAL    NOT NULL CHECK (so_tien > 0),
    ngay_gd     DATETIME NOT NULL,
    FOREIGN KEY (ma_tk) REFERENCES tai_khoan(ma_tk)
);

-- Index hỗ trợ JOIN & lọc theo ngày
CREATE INDEX idx_tk_kh ON tai_khoan(ma_kh);
CREATE INDEX idx_gd_tk ON giao_dich(ma_tk);
CREATE INDEX idx_gd_ngay ON giao_dich(ngay_gd);
-- =====================================================
-- 10 TRUY VẤN SQL - HỆ THỐNG NGÂN HÀNG
-- (SQLite syntax; ghi chú khác biệt cho PostgreSQL/MySQL)
-- =====================================================

-- ---------- Câu 2: 10 KH có số dư cao nhất ----------
-- Số dư là của TÀI KHOẢN -> gộp theo KH để ra tổng số dư mỗi người
SELECT  kh.ma_kh,
        kh.ho_ten,
        kh.tinh_thanh,
        SUM(tk.so_du) AS tong_so_du
FROM    khach_hang kh
JOIN    tai_khoan  tk ON tk.ma_kh = kh.ma_kh
GROUP BY kh.ma_kh, kh.ho_ten, kh.tinh_thanh
ORDER BY tong_so_du DESC
LIMIT 10;

-- ---------- Câu 3: Tổng số & tổng giá trị GD tháng gần nhất ----------
-- "Tháng gần nhất" = tháng của giao dịch mới nhất trong dữ liệu
SELECT  strftime('%Y-%m', MAX(ngay_gd))         AS thang,
        COUNT(*)                                AS so_giao_dich,
        SUM(so_tien)                            AS tong_gia_tri
FROM    giao_dich
WHERE   strftime('%Y-%m', ngay_gd) =
        (SELECT strftime('%Y-%m', MAX(ngay_gd)) FROM giao_dich);

-- ---------- Câu 4: Doanh số theo loại GD (GROUP BY) ----------
SELECT  loai_gd,
        COUNT(*)        AS so_giao_dich,
        SUM(so_tien)    AS tong_gia_tri,
        ROUND(AVG(so_tien), 0) AS gia_tri_tb
FROM    giao_dich
GROUP BY loai_gd
ORDER BY tong_gia_tri DESC;

-- ---------- Câu 5: KH CHƯA từng giao dịch (LEFT JOIN) ----------
SELECT  kh.ma_kh, kh.ho_ten, kh.tinh_thanh
FROM    khach_hang kh
LEFT JOIN tai_khoan tk ON tk.ma_kh = kh.ma_kh
LEFT JOIN giao_dich gd ON gd.ma_tk = tk.ma_tk
WHERE   gd.ma_gd IS NULL          -- không khớp được GD nào
GROUP BY kh.ma_kh, kh.ho_ten, kh.tinh_thanh
ORDER BY kh.ma_kh;

-- ---------- Câu 6: Top 3 KH giá trị GD lớn nhất MỖI tỉnh (window) ----------
WITH gd_theo_kh AS (
    SELECT  kh.tinh_thanh,
            kh.ma_kh,
            kh.ho_ten,
            SUM(gd.so_tien) AS tong_gd
    FROM    khach_hang kh
    JOIN    tai_khoan  tk ON tk.ma_kh = kh.ma_kh
    JOIN    giao_dich  gd ON gd.ma_tk = tk.ma_tk
    GROUP BY kh.tinh_thanh, kh.ma_kh, kh.ho_ten
)
SELECT * FROM (
    SELECT  tinh_thanh, ho_ten, tong_gd,
            ROW_NUMBER() OVER (PARTITION BY tinh_thanh ORDER BY tong_gd DESC) AS hang
    FROM    gd_theo_kh
)
WHERE hang <= 3
ORDER BY tinh_thanh, hang;

-- ---------- Câu 7: Running total theo ngày cho 1 tài khoản ----------
-- Ví dụ tài khoản 1001
SELECT  ngay_gd,
        loai_gd,
        so_tien,
        SUM(so_tien) OVER (ORDER BY ngay_gd
                           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS luy_ke
FROM    giao_dich
WHERE   ma_tk = 1001
ORDER BY ngay_gd
LIMIT 15;

-- ---------- Câu 8: % thay đổi GD tháng này vs tháng trước (LAG) ----------
WITH gd_thang AS (
    SELECT  strftime('%Y-%m', ngay_gd) AS thang,
            SUM(so_tien)               AS tong_thang
    FROM    giao_dich
    GROUP BY strftime('%Y-%m', ngay_gd)
)
SELECT  thang,
        tong_thang,
        LAG(tong_thang) OVER (ORDER BY thang) AS thang_truoc,
        ROUND( 100.0 * (tong_thang - LAG(tong_thang) OVER (ORDER BY thang))
               / LAG(tong_thang) OVER (ORDER BY thang), 1) AS pct_thay_doi
FROM    gd_thang
ORDER BY thang;

-- ---------- Câu 9: GD bất thường (> 3x trung bình của TK đó) ----------
WITH tb_tk AS (
    SELECT ma_tk, AVG(so_tien) AS tb FROM giao_dich GROUP BY ma_tk
)
SELECT  gd.ma_gd, gd.ma_tk, gd.so_tien,
        ROUND(tb_tk.tb, 0)            AS trung_binh_tk,
        ROUND(gd.so_tien / tb_tk.tb, 1) AS so_lan
FROM    giao_dich gd
JOIN    tb_tk ON tb_tk.ma_tk = gd.ma_tk
WHERE   gd.so_tien > 3 * tb_tk.tb
ORDER BY so_lan DESC
LIMIT 15;

-- ---------- Câu 10: CTE - KH có tổng GD vượt 1 tỷ ----------
WITH tong_gd_kh AS (
    SELECT  kh.ma_kh,
            kh.ho_ten,
            kh.tinh_thanh,
            SUM(gd.so_tien) AS tong_giao_dich
    FROM    khach_hang kh
    JOIN    tai_khoan  tk ON tk.ma_kh = kh.ma_kh
    JOIN    giao_dich  gd ON gd.ma_tk = tk.ma_tk
    GROUP BY kh.ma_kh, kh.ho_ten, kh.tinh_thanh
)
SELECT  ma_kh, ho_ten, tinh_thanh, tong_giao_dich
FROM    tong_gd_kh
WHERE   tong_giao_dich > 1000000000     -- 1 tỷ VND
ORDER BY tong_giao_dich DESC;
