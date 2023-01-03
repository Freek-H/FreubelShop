-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Gegenereerd op: 29 dec 2022 om 19:21
-- Serverversie: 10.4.27-MariaDB
-- PHP-versie: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `webshopusers`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `producten`
--

CREATE TABLE `producten` (
  `productID` int(11) NOT NULL,
  `naam` varchar(50) NOT NULL,
  `categorie` varchar(50) NOT NULL,
  `prijs` decimal(10,2) NOT NULL,
  `sterren` int(5) NOT NULL,
  `leverbaar` tinyint(1) NOT NULL,
  `afbeelding_url` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `producten`
--

INSERT INTO `producten` (`productID`, `naam`, `categorie`, `prijs`, `sterren`, `leverbaar`, `afbeelding_url`) VALUES
(1, 'Glitter breinaalden', 'Handwerk', '7.49', 4, 1, 'https://www.hobbygigant.nl/images/detailed/58/Addi-Breinaalden__2-5_jxa8-wn.jpg'),
(12, 'Sudoko', 'Puzzelen', '29.99', 3, 0, 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg/1200px-Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg.png'),
(13, 'Elektro Deken', 'Handig', '99.99', 5, 1, 'https://cdn.shopify.com/s/files/1/0447/5908/9317/products/website1_3_1_1_2000x.png'),
(14, 'Bolletje Wol', 'Knutsel', '3.95', 3, 1, 'https://www.verenadierenartikelen.nl//Files/10/218000/218025/ProductPhotos/620/1871381259.jpg'),
(15, 'Geraniums Plastic', 'Decoratie', '9.00', 3, 1, 'https://www.maxifleur-kunstplanten.nl/media/catalog/product/cache/d6591b9a7cf5ce36d23e2503f5e72818/4/0/407404rdpp10_geranium_40_rood_m_5.jpg'),
(16, 'Salmiak', 'Lekkers', '10.00', 3, 1, 'https://cdn.webshopapp.com/shops/312854/files/364316096/kindlys-kindlys-salmiak-hagel-harde-drop.jpg');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `users`
--

CREATE TABLE `users` (
  `ID` int(50) NOT NULL,
  `Username` text NOT NULL,
  `Password` text NOT NULL,
  `Voornaam` text NOT NULL,
  `Achternaam` text NOT NULL,
  `Geslacht` varchar(50) NOT NULL,
  `Adres` text NOT NULL,
  `Email` text NOT NULL,
  `Geboortedatum` date NOT NULL,
  `Betaling` text NOT NULL,
  `Aflever` text NOT NULL,
  `Telefoon` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `users`
--

INSERT INTO `users` (`ID`, `Username`, `Password`, `Voornaam`, `Achternaam`, `Geslacht`, `Adres`, `Email`, `Geboortedatum`, `Betaling`, `Aflever`, `Telefoon`) VALUES
(42, 'Tonie', '$6$rounds=656000$W0Z0tV46BnZBOYQa$ZpjqWx63R7ndo328Xi/NaD1SNde47Y0GjRQixP9KRUUQpDo1.4YVgjCE4LPINCP/8NN.udzS8Pdv9e5r1xC/L0', 'Tonie', 'Bruijns', 'Man', 'Noordstraat 60', 'toniebruyns@gmail.com', '1995-04-04', 'PayPal', 'Noordstraat 60', 0),
(43, 'Admin', '$6$rounds=656000$pwkW1p5jXfHHAFUA$aCggyfhvHWjC1FAB9tX2dbWdYX23Lo5J6wKkve5j/Dv358wPBTICfkf1OnCW1w9y09W0bc5a7a4CduBeyPj/a/', 'Admin', 'Admin', 'Man', 'Admin', 'Admin', '1990-01-01', 'Credit Card', 'Admin', 0),
(44, 'Fleur', '$6$rounds=656000$DqvdXZG/ycuadGeY$QXX.OUgGQGgdjQaICCzE3vOhoBq49ORxWXpFkwYLqwm15ns/0EC5YBPxkt3j.7pRjHcKEpfWQ8WKF595krzKb.', 'Fleur', 'de Kort', 'Vrouw', 'Dorpslaan 12', 'FleurFlower@gmail.com', '1994-11-10', 'iDeal', 'Dorpslaan 12', 0),
(45, 'Milan', '$6$rounds=656000$5Br.0TtxYql.SWd7$8xwpeMalvApKO6r4SZB9iphqvu4YdingojJ4r.9ayu2t4vEm7x9vjkAOJ3loL1EOnMLX5leb/it5socM/FH5M.', 'Milan', 'Devon', 'Man', 'Merellaan 45', 'MilanoToscano@live.nl', '1990-01-01', 'Credit Card', 'Albert Heijn Dorpsplein', 0),
(47, 'Willem', '$6$rounds=656000$zk2Zohe8rjfwu/Ty$PHCPZSfTBKNLHzvX7/15P.2mvu07R0r5icwOntSdzPr7.UrfybKeWz2r9fMCxTqPMxpwuCyH6/UO6Vvlartmt0', 'Willem', 'Verbaan', 'Man', 'Lelielaan 15', 'WillemVerbaan@hotmail.nl', '0000-00-00', 'iDeal', 'Lelielaan 5', 612345678),
(48, 'Hans', '$6$rounds=656000$GajPdMvjcTzXbv80$6e1sXiJ1nnLCUUgNCUJzr77bIdQ1ghPweEogADdyadFtYTHVn6Hrh1BwU9KfIwfSMVcLtNp/x71JaE5pUD19X/', 'Hans', 'Brink', 'Man', 'Berger 15', 'HansBrink@gmail.com', '0000-00-00', 'iDeal', 'Berger 5', 612345678),
(51, 'Maria', '$6$rounds=656000$hJ/EZ2sT8gXKz9rk$WhNm2kDUAhJc8Ux143t6j8QU22xmTrCGR5YZA0bZWkSveLwCHxWqhcxY/o.dmFa2v3ljaCcy97IjnQYomUUpd/', 'Maria', 'Veras', 'Vrouw', 'Junolaan 3', 'MariaVeras@gmail.com', '1990-01-01', 'iDeal', 'Junolaan 3', 612345678);

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `producten`
--
ALTER TABLE `producten`
  ADD PRIMARY KEY (`productID`);

--
-- Indexen voor tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `producten`
--
ALTER TABLE `producten`
  MODIFY `productID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT voor een tabel `users`
--
ALTER TABLE `users`
  MODIFY `ID` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
