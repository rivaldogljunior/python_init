UPDATE PESSOAENDERECO pe SET pe.cd_municipio = (SELECT m.cd_municipio FROM MUNICIPIO m WHERE m.nm_municipio = ' São Paulo ') WHERE pe.nr_cep = ' 04911120 ';
countCityValid: 1
countCityNull: 0
countExcept: 760
Iniciado em: 19:53:22
Finalizado em: 19:59:05
countCityValid: 0
countCityNull: 0
countExcept: 761
Iniciado em: 20:01:31
Finalizado em: 20:14:08
