-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-08-2024 a las 23:33:39
-- Versión del servidor: 10.1.37-MariaDB
-- Versión de PHP: 7.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `jh`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `idCliente` int(8) NOT NULL,
  `celular` varchar(12) COLLATE utf8_spanish_ci NOT NULL,
  `pais` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `ciudad` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `sector` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `calle` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `foto` longblob NOT NULL,
  `idUsuario` int(8) NOT NULL,
  `idTarjeta` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`idCliente`, `celular`, `pais`, `ciudad`, `sector`, `calle`, `foto`, `idUsuario`, `idTarjeta`) VALUES
(3, '8295637412', 'República Dominicana', 'Santiago', 'Los jardines metroplitanos', 'Mi casa', 0x76616c6f72, 11, NULL),
(4, '8498617224', 'República Dominicana', 'Santiago', 'pekin', 'calle5', 0x76616c6f72, 15, NULL),
(6, '8498617224', 'República Dominicana', 'Santiago', 'pekin', 'calle5', '', 15, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contacto`
--

CREATE TABLE `contacto` (
  `idContacto` int(8) NOT NULL,
  `nombre` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `correo` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` varchar(12) COLLATE utf8_spanish_ci NOT NULL,
  `fecha` date NOT NULL,
  `estado` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `mensaje` text COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `contacto`
--

INSERT INTO `contacto` (`idContacto`, `nombre`, `correo`, `telefono`, `fecha`, `estado`, `mensaje`) VALUES
(1, 'Yerman', 'espinalyerman@gmail.com', '849', '2024-08-09', 'Pendiente', 'hola Como esta'),
(2, 'Yerman Espinal', 'yoto@gmail.com', '849', '2024-08-09', 'Pendiente', 'Hola jose'),
(3, 'Jose miguel', 'yoto4@gmail.com', '2147483647', '2024-08-09', 'Pendiente', 'Hola\r\n'),
(4, 'Jose bello', 'yoto2@gmail.com', '849-861-7224', '2024-08-09', 'Pendiente', 'Hola'),
(5, 'milton', 'yoto3@gmail.com', '849-861-7224', '2024-08-09', 'Pendiente', 'klk palomo'),
(6, 'Yerman', 'espinalyerman@gmail.com', '849-861-7224', '2024-08-09', 'Pendiente', 'hola'),
(7, 'papayo', 'yoel@gmail.com', '8497531594', '2024-08-21', 'Pendiente', 'brrr\r\n'),
(8, 'Yerman', '123456@gmail.com', '849-861-7224', '2024-08-22', 'Pendiente', 'wfd'),
(9, 'Yerman', 'espinalyerman@gmail.com', '849-861-7224', '2024-08-22', 'Pendiente', 'blo'),
(10, 'goku', '123456@gmail.com', '8497531594', '2024-08-23', 'Pendiente', 'bley\r\n');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

CREATE TABLE `factura` (
  `idFactura` int(8) NOT NULL,
  `fecha` date NOT NULL,
  `idServicio` int(8) NOT NULL,
  `idPedido` int(8) NOT NULL,
  `total` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `idPedido` int(8) NOT NULL,
  `fechaPedido` date NOT NULL,
  `estado` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `direccionEnvio` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `idProducto` int(8) NOT NULL,
  `idCliente` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `idProducto` int(8) NOT NULL,
  `nombre` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `cantidad` int(30) NOT NULL,
  `categoria` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `precio` int(30) NOT NULL,
  `imagen` longblob NOT NULL,
  `descripcion` text COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicio`
--

CREATE TABLE `servicio` (
  `idServicio` int(8) NOT NULL,
  `nombre` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `apellido` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `correo` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `tipoServicio` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` varchar(12) COLLATE utf8_spanish_ci NOT NULL,
  `servicioAdicional` varchar(400) COLLATE utf8_spanish_ci NOT NULL,
  `requerimiento` text COLLATE utf8_spanish_ci NOT NULL,
  `enterar` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `fecha` date NOT NULL,
  `precio` int(11) NOT NULL,
  `idCliente` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `servicio`
--

INSERT INTO `servicio` (`idServicio`, `nombre`, `apellido`, `correo`, `tipoServicio`, `telefono`, `servicioAdicional`, `requerimiento`, `enterar`, `fecha`, `precio`, `idCliente`) VALUES
(1, 'Yerman', 'Espinal', 'espinalyerman@gmail.com', 'Mantenimiento', '849-861-7224', '', 'jla', 'Por milton', '2024-08-22', 2000, 6),
(2, 'Yerman', 'Espinal', 'yerman@gmail.com', '', '849-861-7224', '', 'hola', 'asdasdsa', '2024-08-22', 0, 4),
(3, 'Yerman', 'fase4', 'yerman@gmail.com', 'Mantenimiento', '829-777-7777', 'Diseños de jardines', 'yeyey', 'Por jose', '2024-08-22', 2000, 4),
(4, 'Yerman', 'Espinal', 'yerman@gmail.com', 'Mantenimiento', '849-861-7224', '', 'hla', 'Por milton', '2024-08-23', 2000, 4),
(5, 'yiyi', 'Espinal', 'yerman@gmail.com', 'Mantenimiento', '849-861-8988', '', 'yerman', 'sadasdsad', '2024-08-23', 2000, 4),
(9, 'Yerman', 'Espinal', 'yerman@gmail.com', 'Mantenimiento', '849-861-7224', '', 'hola', 'Por milton', '2024-08-23', 2000, 4),
(10, 'Yei', 'Castillo', 'yerman@gmail.com', 'Sistema de detección de plagas', '849-861-7224', 'Poda de planta, Abonado', 'hole', 'por un amigo', '2024-08-23', 5000, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tarjeta`
--

CREATE TABLE `tarjeta` (
  `idTarjeta` int(8) NOT NULL,
  `nomTarjeta` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `numTarjeta` int(16) NOT NULL,
  `fechaExp` date NOT NULL,
  `cvv` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `idUsuario` int(8) NOT NULL,
  `nombre` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `apellido` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `correo` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `contrasena` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `rol` varchar(30) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`idUsuario`, `nombre`, `apellido`, `correo`, `contrasena`, `rol`) VALUES
(11, 'Esmeralda', 'Estrella H.', 'esmeraldastarh@gmail.com', 'sha256$dtTnJGBQDWPNJtVz$a67abc', 'usuario'),
(12, 'Yerman', 'Espinal', 'espinal1@gmail.com', 'sha256$SfVSxfhPBu7R1GRQ$6c3134', 'usuario'),
(13, 'Yerman', 'Espinal', 'espinal1@gmail.com', 'sha256$4FCv98TthcjUbQR5$871c1e', 'usuario'),
(14, 'Yerman', 'Espinal', 'yerman02@gmail.com', 'sha256$ojH3yVqO2i6rYoag$fe1638', 'usuario'),
(15, 'Yerman', 'Espinal', 'yerman@gmail.com', 'sha256$R4AxPsPxc4QMiEuo$01d1c2', 'usuario');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`idCliente`),
  ADD KEY `idUsuario` (`idUsuario`),
  ADD KEY `idTarjeta` (`idTarjeta`);

--
-- Indices de la tabla `contacto`
--
ALTER TABLE `contacto`
  ADD PRIMARY KEY (`idContacto`);

--
-- Indices de la tabla `factura`
--
ALTER TABLE `factura`
  ADD PRIMARY KEY (`idFactura`),
  ADD KEY `idServicio` (`idServicio`,`idPedido`),
  ADD KEY `idPedido` (`idPedido`);

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`idPedido`),
  ADD KEY `idUsuario` (`idProducto`),
  ADD KEY `idCliente` (`idCliente`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`idProducto`);

--
-- Indices de la tabla `servicio`
--
ALTER TABLE `servicio`
  ADD PRIMARY KEY (`idServicio`),
  ADD KEY `idCliente` (`idCliente`);

--
-- Indices de la tabla `tarjeta`
--
ALTER TABLE `tarjeta`
  ADD PRIMARY KEY (`idTarjeta`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idUsuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `idCliente` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `contacto`
--
ALTER TABLE `contacto`
  MODIFY `idContacto` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `factura`
--
ALTER TABLE `factura`
  MODIFY `idFactura` int(8) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `idPedido` int(8) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `idProducto` int(8) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `servicio`
--
ALTER TABLE `servicio`
  MODIFY `idServicio` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `tarjeta`
--
ALTER TABLE `tarjeta`
  MODIFY `idTarjeta` int(8) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idUsuario` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `cliente_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`idUsuario`),
  ADD CONSTRAINT `cliente_ibfk_2` FOREIGN KEY (`idTarjeta`) REFERENCES `tarjeta` (`idTarjeta`);

--
-- Filtros para la tabla `factura`
--
ALTER TABLE `factura`
  ADD CONSTRAINT `factura_ibfk_1` FOREIGN KEY (`idServicio`) REFERENCES `servicio` (`idServicio`),
  ADD CONSTRAINT `factura_ibfk_2` FOREIGN KEY (`idPedido`) REFERENCES `pedidos` (`idPedido`);

--
-- Filtros para la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`idProducto`) REFERENCES `producto` (`idProducto`),
  ADD CONSTRAINT `pedidos_ibfk_2` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`idCliente`);

--
-- Filtros para la tabla `servicio`
--
ALTER TABLE `servicio`
  ADD CONSTRAINT `servicio_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`idCliente`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
