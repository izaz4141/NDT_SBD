-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 02, 2022 at 09:28 AM
-- Server version: 8.0.31
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ndt_sbd`
--

-- --------------------------------------------------------

--
-- Table structure for table `departemen`
--

CREATE TABLE `departemen` (
  `id` varchar(32) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(128) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `departemen`
--

INSERT INTO `departemen` (`id`, `name`) VALUES
('DEP004', 'Finansial'),
('DEP000', 'IT'),
('DEP001', 'Marketing'),
('DEP005', 'Operasional'),
('DEP003', 'Pengembangan dan Perencanaan'),
('DEP002', 'Sumber Daya Manusia');

-- --------------------------------------------------------

--
-- Table structure for table `inventaris`
--

CREATE TABLE `inventaris` (
  `id` varchar(32) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `tipe` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `peminjaman_id` varchar(32) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inventaris`
--

INSERT INTO `inventaris` (`id`, `name`, `tipe`, `peminjaman_id`) VALUES
('1a83141f474e4317af259f397ea66a02', 'Photonic Science', 'Reseptor Citra', NULL),
('1d6528b6595643d894b71ca4959480de', 'ORTEC', 'Detektor NaI(Tl)', NULL),
('23b1db127ccb46eb860f66148af0bebf', 'ORTEC', 'Amplifier', NULL),
('2512765a834a481a9ba0087c374414b3', 'EXCV', 'Kolimator', NULL),
('2eb2d9087ca0442fb19b1f5fa2b8a934', 'Photonic Science', 'Reseptor Citra', NULL),
('3bf10d30006243a2a24a9916eaba24bb', 'Spellman', 'Tabung Sinar-X', NULL),
('40542da099c04c1cbd3b5dd71723fde9', 'ORTEC', 'ADC', NULL),
('4126733c092c482f9788a3e052f0c2bb', 'ASUS', 'Komputer', NULL),
('46f1baaaabfb460fa377561aad32e04b', 'Hitachi Energy', 'HVDC', NULL),
('4cd4777e4e27479fb8f295c949c9a658', 'Bosean', 'Dosimeter', NULL),
('510546a47deb4f5383dbf0467176c7ed', 'ORTEC', 'ADC', NULL),
('51e4a696b730493a9222f81920171584', 'ACER', 'Komputer', NULL),
('540ea3dfecdb498a86d3e9c31cdafc1f', 'Bosean', 'Dosimeter', NULL),
('541dc8cfd7a4443faa454d854c7deed8', 'ORTEC', 'Amplifier', NULL),
('599de66b61064e8297871b3a3bdbe1bf', 'ORTEC', 'Amplifier', NULL),
('5b226e82f9f9452e93e217bd8a8d02a3', 'EXCV', 'Kolimator', NULL),
('5b9ca49966c34ca0ae4ca053f76799f6', 'ORTEC', 'Detektor NaI(Tl)', NULL),
('5cc2136e7bac4e6d80b5b9a7fac8229c', 'ORTEC', 'Detektor NaI(Tl)', NULL),
('604e55281a154c328d7fe40c329e0cba', 'Photonic Science', 'Reseptor Citra', NULL),
('717c1b2782d94a07ac46a9903c01ac29', 'EXCV', 'Kolimator', NULL),
('71e0e3e6b8384deaa232c42dfdfdcf24', 'Bosean', 'Dosimeter', NULL),
('75967a3ab7e945c1a5953fa90caa3497', 'EXCV', 'Tabung Sinar-X', NULL),
('77bbc6f65a1f43acbb6202409e34dd3d', 'ORTEC', 'Detektor NaI(Tl)', NULL),
('7b675cbc2a354242abe0473a73f3cf48', 'ORTEC', 'Detektor NaI(Tl)', NULL),
('7c38a3a58965499c81a61617ce1edf5e', 'Photonic Science', 'Kamera Sinar-X', NULL),
('8c70eb4ecad14749b4c629c223a4daae', 'DELL', 'Monitor', NULL),
('9184d68c4ea847b68a5030dbc4275e99', 'DELL', 'Monitor', NULL),
('929cc5bc5a334f8d9fb46513f141a3da', 'Fujifilm', 'Film Sinar-X', NULL),
('975dc2f2770d4217a0d7dc2c1fe32717', 'ORTEC', 'Amplifier', NULL),
('9c3b7bcdbed144c4816dd60882f65fa0', 'ORTEC', 'Amplifier', NULL),
('9d4ed18ce8594fedaa043f3a6da28836', 'ORTEC', 'HVDC', NULL),
('acdccb787c0b4a5d847fbb0f078febc5', 'DELL', 'Monitor', NULL),
('b01071a39ae54b46921261e4f88e5bfe', 'ORTEC', 'Detektor NaI(Tl)', NULL),
('b2114e27970446f6af2b04481ad27cdd', 'EXCV', 'Kolimator', NULL),
('b58012c135cd4a6ca0277271c6ecfebb', 'ASUS', 'Komputer', NULL),
('bb19382a431d4ea189d5442e9eb389eb', 'Photonic Science', 'Kamera Sinar-X', NULL),
('c2eef906b98b4720aedccd8ba6b4bea9', 'EXCV', 'Tabung Sinar-X', NULL),
('c35cbd2476d2491b8e16019e21ac13c7', 'ORTEC', 'ADC', NULL),
('ca07951533ef455d99db4f3eed03d9b2', 'ORTEC', 'ADC', NULL),
('d3115335a4304d0ab562968d7132aeb5', 'Spellman', 'Tabung Sinar-X', NULL),
('d48572432c0047c8931f2dfb9950ea06', 'Hitachi Energy', 'HVDC', NULL),
('e4ea7b7ca6e64626b672004799038dd0', 'DELL', 'Monitor', NULL),
('e88621e0af1d43d19a96729646e8da3d', 'Photonic Science', 'Reseptor Citra', NULL),
('e8d67e01004744d891f8dc1a08782514', 'ORTEC', 'HVDC', NULL),
('edc566ec84374154a9b34ae369394411', 'Bosean', 'Dosimeter', NULL),
('f03d2b6dee2145aaa88087791b36d4ae', 'EXCV', 'Kolimator', NULL),
('f9a787a8457c483fb92a5acb165649a2', 'ACER', 'Komputer', NULL),
('fdb0ba1981d94d1ba2ed7b1d392ac092', 'EXCV', 'Kolimator', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `karyawan_pekerjaan`
--

CREATE TABLE `karyawan_pekerjaan` (
  `karyawan_id` varchar(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pemesanan_id` varchar(32) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pemesanan`
--

CREATE TABLE `pemesanan` (
  `id` varchar(32) COLLATE utf8mb4_general_ci NOT NULL,
  `lokasi` varchar(345) COLLATE utf8mb4_general_ci NOT NULL,
  `layanan` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `deskripsi` varchar(345) COLLATE utf8mb4_general_ci NOT NULL,
  `pelanggan_id` varchar(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `harga` varchar(128) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `estimasi_pengerjaan` varchar(128) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `tanggal_pemesanan` datetime DEFAULT NULL,
  `tanggal_selesai` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pemesanan`
--

INSERT INTO `pemesanan` (`id`, `lokasi`, `layanan`, `deskripsi`, `pelanggan_id`, `harga`, `estimasi_pengerjaan`, `tanggal_pemesanan`, `tanggal_selesai`) VALUES
('8044ba599001444baa5f16a4c064431b', 'PT Petrokimia Gresik', 'gamma', 'Pipa produksi pupuk plant 1', '0d8f6923d14f4c958f7ae40c316e95bd', NULL, NULL, '2022-12-02 04:24:04', NULL),
('ad33441511334b32b33287bbe21fc0e2', 'Klebengan', 'xray', 'Struktur Bangunan GOR Klebengan', '0d8f6923d14f4c958f7ae40c316e95bd', NULL, NULL, '2022-12-02 04:24:59', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `peminjaman`
--

CREATE TABLE `peminjaman` (
  `id` varchar(32) COLLATE utf8mb4_general_ci NOT NULL,
  `peminjam_id` varchar(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `tanggal_pengambilan` datetime DEFAULT NULL,
  `tanggal_pengembalian` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `peminjaman`
--

INSERT INTO `peminjaman` (`id`, `peminjam_id`, `tanggal_pengambilan`, `tanggal_pengembalian`) VALUES
('d7c0cf2a1fd849f1a3126ea4b228c20e', 'b48de594269d4a72b3f3e29d751d43a5', '2022-12-02 03:44:34', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` varchar(32) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(345) COLLATE utf8mb4_general_ci NOT NULL,
  `password` text COLLATE utf8mb4_general_ci NOT NULL,
  `author_level` int NOT NULL,
  `no_hp` varchar(32) COLLATE utf8mb4_general_ci NOT NULL,
  `departemen_id` varchar(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `date_added` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `email`, `password`, `author_level`, `no_hp`, `departemen_id`, `date_added`) VALUES
('0d8f6923d14f4c958f7ae40c316e95bd', 'Ucok', 'ucok@mail.com', '$2b$12$CqhYbpnVu8Exc3X9VYSRvOw.MqilMnJwuMCWZ3Wi8fQgLImZsxUYW', 2, '0812345678', NULL, '2022-12-02 04:23:21'),
('286fac32c43245658db5495f28ebaa53', 'talia_zuss', 'talia.sulaika.5@gmail.com', '$2b$12$QXPBGFSbW/81pfB1Ch2AfeTdodoSTV81aRPhFQ2QELHgBq4POpAn2', 1, '08129301929', 'DEP004', '2022-12-02 03:51:19'),
('32f935f1a10740efac33c9b9b384aafc', 'jarwasetiawan123', 'jarwasetiawan123@gmail.com', '$2b$12$jQ6TfPOSX410oeTN4JFtLeCQaa9WZD58J/Ve6jKvXBZaWsCzSmLpq', 1, '081231610308', 'DEP001', '2022-12-02 03:53:14'),
('513e1c4c911d4b2eb45340b9c1f3cc35', 'xxkusumasiregarxx', 'kusumasiregar1002@gmail.com', '$2b$12$Qb9w0FMUQMEnsfuvoldw8upxfWtsP3.2YRp.w6uIQRZOlZncB065a', 1, '081291029390', 'DEP003', '2022-12-02 03:49:17'),
('5cbf993475ab499585e5be340f8a2a71', 'Opan Pratama', 'opanpratama123@gmail.com', '$2b$12$jzyC62ovtqQRw8H0ADUO..TWVOCUeWZedrXiA/zwvg6JsK1qdN9GW', 1, '081213201912', 'DEP002', '2022-12-02 03:48:26'),
('5dd686a3d53b4e4991bc97d05685d6d3', 'ardianto.dont.no', 'donoardianto0@gmail.com', '$2b$12$/DREfjIHqp55ts/R6Ll1NOqkE.ffcrl5cXkX9rOgWD.Mh32izEMKq', 1, '08123456789', 'DEP005', '2022-12-02 03:50:15'),
('6c3ba80cfe5f46459f809ab9b5ee3044', 'Yu Zhong', 'yuzhong.sinaga@gmail.com', '$2b$12$W7Q60c1rcOxVaA7yCYkrseyvn74u0.sODptoFyL.1nC/LGDDAo3M6', 1, '089123654789', 'DEP005', '2022-12-02 03:56:04'),
('6d98c4267b844c948c7169a0975fc8ee', 'cinta.luna', 'cintausamah666@gmail.com', '$2b$12$/FvFE2We8mlXu4k5OTHCQearEo7ofTLfD3BMZuAfNoei/L3oeA7f6', 1, '081231939176', 'DEP004', '2022-12-02 03:54:47'),
('b48de594269d4a72b3f3e29d751d43a5', 'Izaz', 'izazwidyan@gmail.com', '$2b$12$Ux9w5pwcdXgA3Neau3zFpOD/ys6p6cGiz/AOKLDfGw/GDKqcSG3eO', 0, '0877777564767', 'DEP000', '2022-12-02 03:25:07'),
('d22eba0859c2426681f4e05305469ba3', 'Dimas januar', 'dimasdimasdimas@gmail.com', '$2b$12$ZGI4tXUORgxJ4qi4YbV7zex0XJ7hYcJK6eq5Xbbb.QkDi5//aqHKK', 1, '08129391939', 'DEP005', '2022-12-02 03:53:52'),
('da989f83eff24c949d9bf7fc3f7406e4', 'aisyah.purnawati', 'aisyahpurnawatisiregar@gmail.com', '$2b$12$CmaLlhO3v78wvAh2ixtb1uUAebFLH9X/NXQLxTtl2XtpBAq5DUNPa', 2, '089089089089', NULL, '2022-12-02 03:55:21'),
('ee66c5d4846c4aa49fb0b60b8d1ec7b0', 'Asep Saepuloh', 'asepsaepuloh@gmail.com', '$2b$12$wouIHQycHo9EaeJS57sGQ.8ZnMx2EPGB3tYvZvTGCZK0G0pIwdu96', 2, '081312000005', NULL, '2022-12-02 03:46:22'),
('eeed746a9c5a4922b515ce55220b6864', 'satriogilang', 'satrioisma@gmail.com', '$2b$12$FzI8j44OQGOvhnREBqHwfelVsqhvY8ArM0A7xSTcsHFGbAD.xzoTC', 0, '14045', 'DEP000', '2022-12-02 04:19:27'),
('f81c6974e69841d3811c2e03d55150e1', 'dinda uyainah', 'uyainah.dinda.111102@gmail.com', '$2b$12$XPBF//Mx3Muh1ngk3loJW.8E20qfbBZ2tvIO6o.NNBFVcAw2FiYy.', 2, '081312106005', NULL, '2022-12-02 03:52:01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `departemen`
--
ALTER TABLE `departemen`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `inventaris`
--
ALTER TABLE `inventaris`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `peminjaman_id` (`peminjaman_id`);

--
-- Indexes for table `karyawan_pekerjaan`
--
ALTER TABLE `karyawan_pekerjaan`
  ADD KEY `karyawan_id` (`karyawan_id`),
  ADD KEY `pemesanan_id` (`pemesanan_id`);

--
-- Indexes for table `pemesanan`
--
ALTER TABLE `pemesanan`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `pelanggan_id` (`pelanggan_id`);

--
-- Indexes for table `peminjaman`
--
ALTER TABLE `peminjaman`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `peminjam_id` (`peminjam_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `no_hp` (`no_hp`),
  ADD KEY `departemen_id` (`departemen_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `inventaris`
--
ALTER TABLE `inventaris`
  ADD CONSTRAINT `inventaris_ibfk_1` FOREIGN KEY (`peminjaman_id`) REFERENCES `peminjaman` (`id`);

--
-- Constraints for table `karyawan_pekerjaan`
--
ALTER TABLE `karyawan_pekerjaan`
  ADD CONSTRAINT `karyawan_pekerjaan_ibfk_1` FOREIGN KEY (`karyawan_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `karyawan_pekerjaan_ibfk_2` FOREIGN KEY (`pemesanan_id`) REFERENCES `pemesanan` (`id`);

--
-- Constraints for table `pemesanan`
--
ALTER TABLE `pemesanan`
  ADD CONSTRAINT `pemesanan_ibfk_1` FOREIGN KEY (`pelanggan_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `peminjaman`
--
ALTER TABLE `peminjaman`
  ADD CONSTRAINT `peminjaman_ibfk_1` FOREIGN KEY (`peminjam_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`departemen_id`) REFERENCES `departemen` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
