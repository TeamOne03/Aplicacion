-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-08-2024 a las 23:20:15
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
  `celular` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
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
(7, '8299681952', 'República Dominicana', 'Santiago', 'pekin', '12', 0x76616c6f72, 11, 8),
(8, '8299689000', 'República Dominicana', 'Santiago', 'ensanche espaillat', '12', 0x76616c6f72, 12, 11),
(9, '8299681952', 'República Dominicana', 'Santiago', 'los jardines metropolitanos', 'la mina', 0x76616c6f72, 13, 12);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contacto`
--

CREATE TABLE `contacto` (
  `idContacto` int(8) NOT NULL,
  `nombre` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `correo` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` int(12) NOT NULL,
  `fecha` date NOT NULL,
  `estado` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `mensaje` text COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

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
  `Productos` int(80) NOT NULL,
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
  `subcategoria` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `precio` int(30) NOT NULL,
  `imagen` varchar(500) COLLATE utf8_spanish_ci NOT NULL,
  `descripcion` text COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`idProducto`, `nombre`, `cantidad`, `categoria`, `subcategoria`, `precio`, `imagen`, `descripcion`) VALUES
(1, 'Manguera', 50, 'masvendidos', '', 1975, 'mangueraVerde.jpg', 'Descubre la herramienta esencial para mantener tu jardín exuberante y vibrante con nuestra manguera de jardín de alta calidad. Fabricada con materiales duraderos y resistentes a la intemperie, esta manguera ofrece una flexibilidad excepcional para llegar a cada rincón de tu jardín con facilidad. Su diseño ligero y manejable permite un uso cómodo y sin esfuerzo, mientras que su construcción anti-torsión garantiza un flujo de agua constante y sin obstrucciones.'),
(2, 'Abono', 50, 'masvendidos', '', 500, 'abono.png', 'Transforma tu jardín en un paraíso de vitalidad y verdor con nuestro abono premium, la solución perfecta para nutrir tus plantas y promover un crecimiento saludable. Formulado con una mezcla equilibrada de nutrientes orgánicos de alta calidad, nuestro abono proporciona a tus plantas los elementos esenciales que necesitan para florecer. Su composición rica en materia orgánica mejora la estructura del suelo, promoviendo la retención de agua y nutrientes, así como la actividad microbiana beneficiosa. flores vibrantes y cultivos abundantes, ¡haciendo de tu jardín un espectáculo de color y vida!'),
(3, 'Planta', 50, 'masvendidos', '', 375, 'planta.jpg', 'Conoce a nuestra encantadora y versátil Begonia Rex, una joya botánica que añadirá un toque de elegancia y exotismo a cualquier espacio interior. Con sus hojas grandes y exuberantes, adornadas con intrincados patrones y una paleta de colores que van desde el verde esmeralda hasta el plateado y el rosa, esta planta cautivadora es una obra de arte viviente.'),
(4, 'Pulverizador', 50, 'masvendidos', '', 500, 'pulverizador12.jpg', 'Nuestro pulverizador de jardín de alto rendimiento, la herramienta imprescindible para facilitar tus labores de cuidado y mantenimiento del jardín. Diseñado con la combinación perfecta de durabilidad, eficiencia y comodidad, este pulverizador te ofrece un control preciso y una distribución uniforme de líquidos, ya sea para regar plantas, aplicar fertilizantes o combatir plagas.'),
(5, 'Tijeras', 50, 'masvendidos', '', 1275, 'tijerasStanley.jpg', 'Descubre la herramienta imprescindible para dar forma y cuidar tus plantas con precisión y facilidad: nuestras tijeras de jardín de primera calidad. Diseñadas con un equilibrio perfecto entre durabilidad, comodidad y eficacia, estas tijeras te brindan un corte limpio y preciso en cada uso. Fabricadas con acero inoxidable de alta calidad, las hojas afiladas de nuestras tijeras garantizan una acción de corte suave y sin esfuerzo, permitiéndote podar, cortar y dar forma a tus plantas con la máxima precisión y cuidado.'),
(6, 'Podadora de Césped', 50, 'masvendidos', '', 6350, 'podadora-de-cesped.webp', 'Esta podadora es el compañero perfecto para aquellos que buscan mantener su jardín impecable y bien cuidado. Con su diseño ergonómico y empuñadura antideslizante, proporciona un agarre cómodo y seguro, permitiéndote realizar cortes precisos con facilidad y sin fatiga. Con este modelo mejorado, la podadora ahora cuenta con una función de ajuste de altura intuitiva, que te permite adaptar la altura de corte según las necesidades específicas de tu césped.'),
(7, 'Maceta', 50, 'masvendidos', '', 500, 'maceta.jpg', 'Esta maceta, con su construcción duradera y resistente a la intemperie, es una compañera confiable para embellecer tu entorno durante todas las estaciones del año. Además, su amplio tamaño proporciona un espacio óptimo para que las raíces crezcan libremente, fomentando un desarrollo saludable de tus plantas favoritas. Su diseño funcional incluye un sistema de drenaje inteligente que mantiene el equilibrio hídrico adecuado para las plantas, facilitando su cuidado y mantenimiento.'),
(8, 'Ficus elastica', 50, 'masvendidos', '', 250, 'PLANTA-FICUS-ELASTICA-ROBUSTA-1-.jpg', 'Los Ficus son plantas de interior que requieren un riego cuidadoso. Se debe regar cada 6 o 7 días, evitando el encharcamiento y asegurándose de mantener el sustrato húmedo. Además, es recomendable fertilizar quincenalmente con TRIPLE 15 o abonar la tierra para proporcionar los nutrientes necesarios para un crecimiento saludable. Con estos cuidados adecuados, tu Ficus prosperará y lucirá exuberante en tu hogar. Recuerda también proporcionarle luz indirecta y mantenerlo alejado de corrientes de aire para garantizar su bienestar óptimo.'),
(9, 'Aspersor', 50, 'masvendidos', '', 500, 'aspersor.jpg', 'El aspersor de 0,6 litros de capacidad es la herramienta ideal para mantener tu jardín siempre verde y exuberante. Con su diseño compacto y eficiente, este aspersor ofrece una distribución uniforme del agua, cubriendo áreas extensas con facilidad. Su cabezal ajustable te permite controlar el patrón de riego según las necesidades de tu jardín, desde un rocío suave hasta un chorro más potente.'),
(10, 'Alimento para orquídeas', 50, 'masvendidos', '', 355, 'crecemasorquideas.jpg', 'Logra que estén más sanas, activen nuevos brotes y desarrollen flores más grandes, coloridas y un follaje verde y hermoso. Importante recordar no excederse con el riego. Frecuencia: cada 20 días. Este alimento es adecuado para cualquier época del año.'),
(11, 'Maceta de cemento', 50, 'masvendidos', '', 1500, 'Matera-Redonda-Cemento.jpg', 'Maceta de fibra de arena y concreto Medidas: 25 cm de alto x 25 cm de diámetro x 21 cm de largo. La maceta de cemento es mucho más que un simple recipiente para tus plantas; es una declaración de estilo y durabilidad para tu hogar. Con su diseño moderno y minimalista, esta maceta añade un toque de elegancia a cualquier espacio interior o exterior.'),
(12, 'Pala de madera', 50, 'masvendidos', '', 118, 'palademadera.jpg', 'Fabricación en acero carbono especial de alta calidad. Recibe pintura electrostática a polvo, que tiene mejor presentación visual y mayor protección contra la oxidación. El mango de esta herramienta, además de tener excelente resistencia, se fabrica con madera de origen renovable. Mango con terminación barnizada para una mejor presentación del producto. La capa protectora de barniz incoloro realza su tonalidad.'),
(13, 'Petunia larga vida', 30, 'plantas', 'Plantas florales', 350, 'PLANTA-PETUNIA-LARGA-VIDA-2-.jpg', 'La Petunia Larga Vida es una planta de exterior, el riego se hace cada 4 o 5 días evitando encharcamiento y manteniendo el sustrato húmedo. Se recomienda fertilizar quincenalmente con florescencia o abonar la tierra. El mantenimiento se hace quitando flores y hojas secas. En temporadas húmedas como el invierno se recomienda disminuir el riego y en temporadas cálidas aumentarlo según la necesidad ambiental. También se recomienda atomizar las hojas con agua para crear un ambiente más húmedo.'),
(14, 'Lavanda', 30, 'plantas', 'Plantas aromaticas', 475, 'PLANTA-LAVANDA-2-.jpg', 'La lavanda es una planta herbácea aromática conocida por su distintivo aroma floral y sus espigas de flores moradas. Con hojas estrechas y lanceoladas de un tono verde grisáceo, la lavanda crece en matas compactas que pueden alcanzar alturas de hasta 60 centímetros. Sus flores, dispuestas en racimos terminales, desprenden un aroma relajante y fresco que atrae a abejas y otros polinizadores.'),
(15, 'Ficus elastica', 30, 'plantas', 'Plantas no florales', 250, 'PLANTA-FICUS-ELASTICA-ROBUSTA-1-.jpg', 'Los Ficus son plantas de interior que requieren un riego cuidadoso. Se debe regar cada 6 o 7 días, evitando el encharcamiento y asegurándose de mantener el sustrato húmedo. Además, es recomendable fertilizar quincenalmente con TRIPLE 15 o abonar la tierra para proporcionar los nutrientes necesarios para un crecimiento saludable. Con estos cuidados adecuados, tu Ficus prosperará y lucirá exuberante en tu hogar. Recuerda también proporcionarle luz indirecta y mantenerlo alejado de corrientes de aire para garantizar su bienestar óptimo.'),
(16, 'Anthurium blanca', 30, 'plantas', 'Plantas florales', 550, 'PLANTA-ANTURIO-BLANCA.jpg', 'El Anthurium scherzerianum es una planta de interior que prefiere lugares iluminados con luz natural. El riego debe hacerse cada 3 días, evitando el encharcamiento. Se recomienda usar un plato con piedrillas y agua en la base para que la planta la absorba por capilaridad (llenar el plato a aproximadamente 2 cm). Pulverizar las hojas frecuentemente y abonar quincenalmente con fertilizantes para floración.'),
(17, 'Orquídea morada', 30, 'plantas', 'Plantas florales', 1250, 'Orquidea-morada.png', 'La orquídea Phalaenopsis hybrid es una Orchidaceae de origen asiático, perfecta para decorar espacios de interior bien iluminados sin sol directo. Deja que la planta se seque entre riegos (riego por inmersión con agua mineral o reposada). El trasplante se realiza después de la floración, utilizando sustratos especiales para orquídeas y manteniendo medidas higiénicas para evitar enfermedades debido al estrés del trasplante. Abona un mes después del trasplante con fertilizantes especiales para orquídeas.'),
(18, 'Kalanchoe', 30, 'plantas', 'Plantas florales', 250, 'KALANCHOE-2.png', 'El Kalanchoe es una planta versátil adecuada tanto para interiores como exteriores, ofreciendo una belleza duradera con sus vibrantes flores y follaje exuberante. Su cuidado es sencillo: riego regular cada cuatro días es fundamental para mantener un equilibrio hídrico óptimo, evitando el encharcamiento pero asegurando que el sustrato permanezca ligeramente húmedo. Se recomienda fertilizar quincenalmente con un fertilizante específico para flores o abonar el suelo con nutrientes adecuados.'),
(19, 'Planta', 30, 'plantas', 'Plantas no florales', 375, 'planta.jpg', 'Conoce a nuestra encantadora y versátil Begonia Rex, una joya botánica que añadirá un toque de elegancia y exotismo a cualquier espacio interior. Con sus hojas grandes y exuberantes, adornadas con intrincados patrones y una paleta de colores que van desde el verde esmeralda hasta el plateado y el rosa, esta planta cautivadora es una obra de arte viviente.'),
(20, 'Rosas kordanas', 30, 'plantas', 'Plantas florales', 1500, 'rosa-kordana.jpg', 'El Rosal Mini Kordana es una especie de rosa en tamaño reducido, ideal para exteriores y que requiere luz solar para florecer. Sus cuidados son similares a los de las rosas comunes, y puede presentar una amplia variedad de colores y formas.'),
(21, 'Alimento para cactus', 30, 'fertilizantes', 'Fertilizante para flores', 313, 'fertilizantecrecemas.jpg', 'En macetas chicas vierta media tapa de Crece Más directamente en la tierra. En macetas medianas y grandes utilizar 2 tapas por maceta directamente en la tierra. Luego regar en la forma acostumbrada. Frecuencia: cada 15 días. Este alimento es adecuado para cualquier época del año.'),
(22, 'Fertilizante foliar', 30, 'fertilizantes', 'Fertilizante para flores', 529, 'fertilizantefoliar.jpg', 'El fertilizante foliar para todas las plantas GRAN AMOR es de fácil aplicación, proporcionando nutrientes y micro-elementos indispensables para el desarrollo de las plantas de interior y exterior, siendo también muy recomendable para hierbas aromáticas, helechos y orquídeas. Acelera el crecimiento, desarrollando flores más grandes, activando nuevos brotes, raíces más fuertes y un follaje más verde, sano y exuberante.'),
(23, 'Crece más', 30, 'fertilizantes', 'Vitaminas de crecimiento', 330, 'crecemas.jpg', 'Utilizar la tapa del envase como medida. En macetas chicas y medianas vierta en la tierra ½ tapa. En macetas grandes vierta 1 tapa. Luego regar en la forma acostumbrada. Frecuencia: aplicar cada 20 días.'),
(24, 'Activador de flores', 30, 'fertilizantes', 'Fertilizante para flores', 310, 'crecemasactivador.jpg', 'Proporciona una equilibrada composición de nutrientes y micro elementos que provoca un acelerado desarrollo de pimpollos. Este activador es efectivo para almácigos, plantas que estén en macetas o directamente en tierra.'),
(25, 'Alimento orquídeas', 30, 'fertilizantes', 'Fertilizante para flores', 355, 'crecemasorquideas.jpg', 'Logra que estén más sanas, activen nuevos brotes y desarrollen flores más grandes, coloridas y un follaje verde y hermoso. Importante recordar no excederse con el riego. Frecuencia: cada 20 días. Este alimento es adecuado para cualquier época del año.'),
(26, 'Crece raíces', 30, 'fertilizantes', 'Fertilizante de raices', 293, 'crecemasraices.jpg', 'Perfecto cuando se trasplantan brotes, gajos, estacas o plantas, acelerando formidablemente el desarrollo de las raíces. Desarrolla las raíces a plantas que estén en macetas o en la tierra. Frecuencia: Aplicar cada 15 días. Este alimento es adecuado para cualquier época del año.'),
(27, 'Nurish', 30, 'fertilizantes', 'Vitaminas para el suelo', 107, 'nurish.jpg', 'NURISH 20-20-20 es un abono foliar que aporta nutrientes en forma instantánea a todas las especies vegetales, gramíneas, frutales y ornamentales a través de las hojas. NURISH es muy seguro y eficiente para las plantas. En plantas ornamentales disuelva una cucharada en un galón de agua y aplique cada 15 a 21 días.'),
(28, 'Nurish 3lb', 30, 'fertilizantes', 'Vitaminas para el suelo', 296, 'nurish2.jpg', 'NURISH es un abono foliar que aporta nutrientes en forma instantánea a todas las especies vegetales, gramíneas, frutales y ornamentales a través de las hojas. NURISH es muy seguro y eficiente para las plantas. Elementos solubles en el agua. Abono foliar libre de Cloro Micronutrientes Quelatados.'),
(29, 'Pala de madera', 30, 'herramientas', 'Palas', 118, 'palademadera.jpg', 'Fabricación en acero carbono especial de alta calidad. Recibe pintura electrostática a polvo, que tiene mejor presentación visual y mayor protección contra la oxidación. El mango de esta herramienta, además de tener excelente resistencia, se fabrica con madera de origen renovable. Mango con terminación barnizada para una mejor presentación del producto. La capa protectora de barniz incoloro realza su tonalidad.'),
(30, 'Pala ancha', 30, 'herramientas', 'Palas', 112, 'palaancha.jpg', 'Fabricación en acero carbono especial de alta calidad. Recibe pintura electrostática a polvo, que tiene mejor presentación visual y mayor protección contra la oxidación. Además, este proceso garantiza una durabilidad excepcional, resistente a los elementos adversos. Su acabado suave y uniforme realza su apariencia, convirtiéndolo en un componente estético y funcional para cualquier entorno.'),
(31, 'Rastrillo', 30, 'herramientas', 'Rastrillos', 147, 'rrastrillo.webp', 'Se aplica principalmente para ablandar la tierra y retirar residuos. Fabricación en acero carbono especial de alta calidad. Recibe pintura electrostática a polvo, que tiene mejor presentación visual y mayor protección contra la oxidación. Este método es fundamental para preparar el terreno de manera eficiente, facilitando diversas tareas agrícolas y de construcción. Su construcción en acero carbono especial garantiza resistencia y durabilidad excepcionales.'),
(32, 'Arrancador de yuyos', 30, 'herramientas', 'Arrancadores de yuyos', 92, 'arrancadordeyuyos.webp', 'Diseño ergonómico y robusto. Uso para jardín. Diseñado para facilitar la extracción de malezas no deseadas, como hierbas y arbustos, desde la raíz. Compuesto por un mango ergonómico que proporciona un agarre cómodo y seguro, este dispositivo incorpora una punta afilada o una garra dentada en su extremo, diseñada para penetrar en el suelo con facilidad y arrancar las plantas no deseadas con eficacia.'),
(33, 'Manguera', 30, 'herramientas', 'Mangueras', 1975, 'manguera.jpg', 'Descubre la herramienta esencial para mantener tu jardín exuberante y vibrante con nuestra manguera de jardín de alta calidad. Fabricada con materiales duraderos y resistentes a la intemperie, esta manguera ofrece una flexibilidad excepcional para llegar a cada rincón de tu jardín con facilidad. Su diseño ligero y manejable permite un uso cómodo y sin esfuerzo, mientras que su construcción anti-torsión garantiza un flujo de agua constante y sin obstrucciones.'),
(34, 'Pistola de manguera', 30, 'herramientas', 'Pistolas de mangueras', 377, 'pistolademanguera.jpg', 'Pistola forrada en caucho. Controla el flujo de agua. Brinda máxima comodidad. Mango ergonómico. Mide 6 pulgadas. Esencial para controlar el flujo de agua de una manguera de jardín. Consta típicamente de un cuerpo ergonómico que se adapta cómodamente a la mano del usuario y un gatillo de fácil accionamiento para regular el flujo de agua con precisión.'),
(35, 'Tijeras de jardin', 30, 'herramientas', 'Tijeras', 1275, 'tijerasStanley.jpg', 'Descubre la herramienta imprescindible para dar forma y cuidar tus plantas con precisión y facilidad: nuestras tijeras de jardín de primera calidad. Diseñadas con un equilibrio perfecto entre durabilidad, comodidad y eficacia, estas tijeras te brindan un corte limpio y preciso en cada uso. Fabricadas con acero inoxidable de alta calidad, las hojas afiladas de nuestras tijeras garantizan una acción de corte suave y sin esfuerzo, permitiéndote podar, cortar y dar forma a tus plantas con la máxima precisión y cuidado.'),
(36, 'Juego de jardin', 30, 'herramientas', 'Palas', 1416, 'JUEGO-JARDIN-3-PIEZAS-M.MADERA-PALAS-RASTRILLO.jpg', 'RASTRILLO: Ideal para remover la tierra compactada. CUCHARA: Grande ideal para cavar. TRANSPLANTADOR: Utilizado en horticultura para cavar y realizar trasplantes. Es un conjunto versátil de herramientas diseñadas para una variedad de tareas de jardinería y paisajismo.'),
(37, 'Aspersor', 30, 'accesorios', 'Aspersores', 232, 'aspersor.jpg', 'El aspersor de 0,6 litros de capacidad es la herramienta ideal para mantener tu jardín siempre verde y exuberante. Con su diseño compacto y eficiente, este aspersor ofrece una distribución uniforme del agua, cubriendo áreas extensas con facilidad. Su cabezal ajustable te permite controlar el patrón de riego según las necesidades de tu jardín, desde un rocío suave hasta un chorro más potente.'),
(38, 'Base con ruedas', 30, 'accesorios', 'Bases', 300, 'BaseRodachin.jpg', 'Base redonda para matera. Al ser de plástico podrás tenerlo tanto interior como en exterior. Hecha de plástico resistente, esta base está diseñada para resistir las inclemencias del tiempo, permitiéndote embellecer tanto tus espacios interiores como exteriores. Ya sea que desees añadir un toque de verde a tu sala de estar o crear un oasis de serenidad en tu patio, esta base para matera es la elección perfecta.'),
(39, 'Pulverizador', 30, 'accesorios', 'Aspersores', 500, 'pulverizador12.jpg', 'Nuestro pulverizador de jardín de alto rendimiento, la herramienta imprescindible para facilitar tus labores de cuidado y mantenimiento del jardín. Diseñado con la combinación perfecta de durabilidad, eficiencia y comodidad, este pulverizador te ofrece un control preciso y una distribución uniforme de líquidos, ya sea para regar plantas, aplicar fertilizantes o combatir plagas.'),
(40, 'Regadera', 30, 'accesorios', 'Regaderas', 500, 'regadera.jpg', 'Capacidad de 1,8 litros. El pequeño orificio garantiza un riego preciso. También hay atomizadores disponibles en la misma colección. Nuestra regadera es el compañero perfecto para tus plantas, diseñada para brindar la cantidad justa de agua con precisión y facilidad. Con su boquilla ergonómica y su mango cómodo, regar tus plantas se convierte en una tarea sencilla y placentera.'),
(41, 'Maceta de cemento', 30, 'accesorios', 'Macetas', 1500, 'Matera-Redonda-Cemento.jpg', 'Maceta de fibra de arena y concreto Medidas: 25 cm de alto x 25 cm de diámetro x 21 cm de largo. La maceta de cemento es mucho más que un simple recipiente para tus plantas; es una declaración de estilo y durabilidad para tu hogar. Con su diseño moderno y minimalista, esta maceta añade un toque de elegancia a cualquier espacio interior o exterior.'),
(42, 'Maceta plastica', 30, 'accesorios', 'Macetas', 230, 'maceta-verde-18.jpg', 'Perfectas para interiores y exteriores. Posee agujero para el drenaje del agua. Nuestra maceta plástica de color verde es una combinación perfecta de estilo y funcionalidad para tus plantas. Con su tono verde vibrante, añade un toque refrescante a cualquier espacio interior o exterior. Fabricada con materiales de alta calidad, esta maceta es resistente y duradera, proporcionando un hogar seguro y elegante para tus plantas favoritas.'),
(43, 'Maceta', 30, 'accesorios', 'Macetas', 500, 'maceta.jpg', 'Esta maceta, con su construcción duradera y resistente a la intemperie, es una compañera confiable para embellecer tu entorno durante todas las estaciones del año. Además, su amplio tamaño proporciona un espacio óptimo para que las raíces crezcan libremente, fomentando un desarrollo saludable de tus plantas favoritas. Su diseño funcional incluye un sistema de drenaje inteligente que mantiene el equilibrio hídrico adecuado para las plantas, facilitando su cuidado y mantenimiento.'),
(44, 'Aspersor oscilante', 30, 'accesorios', 'Aspersores', 2000, 'aspersor2.jpg', '20 boquillas de precisión proporcionan una cobertura máxima de hasta 4,500 pies cuadrados para césped saludable y jardines en crecimiento. Nuestro aspersor es la solución perfecta para mantener tu jardín exuberante y verde con un mínimo esfuerzo. Con su diseño innovador y eficiente, este aspersor proporciona una distribución uniforme de agua, cubriendo grandes áreas de tu jardín con facilidad.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicio`
--

CREATE TABLE `servicio` (
  `idServicio` int(8) NOT NULL,
  `tipo` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `precio` int(30) NOT NULL,
  `descripcion` text COLLATE utf8_spanish_ci NOT NULL,
  `fechaSolicitud` date NOT NULL,
  `idCliente` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tarjeta`
--

CREATE TABLE `tarjeta` (
  `idTarjeta` int(11) NOT NULL,
  `idCliente` int(8) NOT NULL,
  `nomTarjeta` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `numTarjeta` int(16) NOT NULL,
  `fechaExp` date NOT NULL,
  `cvv` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `tarjeta`
--

INSERT INTO `tarjeta` (`idTarjeta`, `idCliente`, `nomTarjeta`, `numTarjeta`, `fechaExp`, `cvv`) VALUES
(4, 7, 'milton', 2147483647, '2024-01-01', 123),
(8, 7, 'visa', 4545, '2024-01-01', 123),
(10, 8, 'visa', 5454, '2030-03-01', 159),
(11, 8, 'visa', 4454, '2024-01-01', 454),
(12, 9, 'visa', 4545, '2028-08-01', 598);

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
(11, 'milton', 'valerio', 'milton@gmail.com', 'sha256$G9gAehyBcIuoS7g9$ee3420', 'usuario'),
(12, 'albiery', 'perez', 'albiery@gmail.com', 'sha256$xk5xPpz0kZHfBDOM$58d93e', 'usuario'),
(13, 'Esmeralda', 'Ruby', 'zafiro@gmail.com', 'sha256$kcTvu3mEEKDSNv8R$afa014', 'usuario');

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
  ADD PRIMARY KEY (`idTarjeta`),
  ADD KEY `idCliente` (`idCliente`);

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
  MODIFY `idCliente` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `contacto`
--
ALTER TABLE `contacto`
  MODIFY `idContacto` int(8) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `factura`
--
ALTER TABLE `factura`
  MODIFY `idFactura` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `idPedido` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `idProducto` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT de la tabla `servicio`
--
ALTER TABLE `servicio`
  MODIFY `idServicio` int(8) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tarjeta`
--
ALTER TABLE `tarjeta`
  MODIFY `idTarjeta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idUsuario` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

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
  ADD CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`Productos`) REFERENCES `producto` (`idProducto`),
  ADD CONSTRAINT `pedidos_ibfk_2` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`idCliente`);

--
-- Filtros para la tabla `servicio`
--
ALTER TABLE `servicio`
  ADD CONSTRAINT `servicio_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`idCliente`);

--
-- Filtros para la tabla `tarjeta`
--
ALTER TABLE `tarjeta`
  ADD CONSTRAINT `tarjeta_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`idCliente`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
