-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3309
-- Tiempo de generación: 26-04-2023 a las 05:13:30
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_contactos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contacto`
--

CREATE TABLE `contacto` (
  `cont_id` int(11) NOT NULL,
  `cont_nombres` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `cont_apellidos` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `cont_telefono` bigint(20) NOT NULL,
  `cont_correo` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `cont_imagen` varchar(100) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `contacto`
--

INSERT INTO `contacto` (`cont_id`, `cont_nombres`, `cont_apellidos`, `cont_telefono`, `cont_correo`, `cont_imagen`) VALUES
(33, 'Carlos Duty', 'Martinez Gutierrez', 321456789, 'carlos@hotmail.com', '2023212501icon4.png'),
(34, 'Kristina Isabbelle ', 'Orozco Puertas', 314567898, 'Kris@gmail.com', '2023212613icon1.png'),
(35, 'Yolanda Maria', 'de la trinidad gomez', 3214567854, 'gomez@gmail.com', '2023212740icon3.png'),
(36, 'Federico Antonio', 'Cincopalacios Guerra', 3214876576, 'guerra@gmail.com', '2023212908icon2.png'),
(39, 'yolanda maria', 'de la trinidad savava', 123456, 'yola@gmail.com', '2023213709namtabatman.png');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `contacto`
--
ALTER TABLE `contacto`
  ADD PRIMARY KEY (`cont_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `contacto`
--
ALTER TABLE `contacto`
  MODIFY `cont_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
