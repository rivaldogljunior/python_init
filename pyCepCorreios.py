from pycep_correios import get_address_from_cep, WebService, exceptions
from datetime import datetime
hora_atual = datetime.now()
date_init = hora_atual.strftime('%H:%M:%S')


ceps = ['89826200', '84100000', '07800000', '04911120', '07908090', '84100000', '08005466', '75664970', '69710000', '86560000', '05350901', '78617000', '72370000', '02920222', '44149999', '76890010', '99704046', '44149999', '44149999', '85353030', '05091903', '71230000', '78232000', '01000000', '44149999', '99100000', '88742508', '89000000', '82020000', '95900995', '86655000', '06029900', '70092900', '72000000', '72000000', '72000000', '72000000', '72300000', '72190000', '72145000', '72000000', '06750000', '75599970', '72000000', '72600000', '72000000', '72000000', '72000000', '72000000', '72000000', '86603680', '72300000', '72370000', '72370330', '72370000', '72000000', '72000000', '72000001', '78232000', '72000000', '72000000', '72000000', '72000000', '72465700', '71904510', '72300000', '72000000', '99100000', '84100000', '72370000', '72370000', '78232000', '78232000', '78232000', '89881540', '71120500', '72370000', '72300000', '72370000', '72370330', '72370330', '72300000', '89644000', '72370330', '72370000', '72300000', '78232000', '78232000', '00089600', '78232000', '72370000', '72370000', '72370330', '72370000', '72370000', '72370000', '72370000', '72370000', '72370000', '72370000', '72370000', '72370310', '72370000', '72370000', '72370000', '72370330', '72370000', '72000000', '72000000', '86556000', '76421000', '72370000', '72370000', '72000000', '72370000', '72090000', '44100100', '44149999', '99100000', '89861700', '69710000', '07980068', '89699000', '44149999', '72000000', '72000000', '72000000', '72000000', '44149999', '72000000', '72000001', '88821515', '72370000', '72000000', '72300000', '72000000', '72000000', '72000000', '84100000', '95887000', '45833999', '44149999', '44100000', '44100000', '07843080', '44149999', '62100000', '44149999', '38480000', '89625000', '38480000', '38480000', '01046925', '38480000', '38475000', '75602970', '02362206', '79888000', '44149999', '55333000', '38475000', '05093901', '25931970', '78100000', '06886990', '89510000', '07700000', '44149999', '38480000', '89712054', '06290027', '44149999', '84100000', '99915000', '38475000', '88338900', '68209002', '44149999', '44149999', '78232000', '06700000', '05586100', '28948890', '07942230', '78232000', '71608971', '72000000', '78100000', '98705000', '77654970', '77654970', '77654970', '76866970', '38484434', '38480000', '44100000', '44149999', '44149999', '38480000', '38480000', '87907020', '38480000', '38480000', '88202020', '38480000', '89712060', '89712060', '75924970', '72701994', '06700999', '07904196', '07900000', '78165900', '07800000', '78232000', '72700000', '85836000', '75655000', '72370000', '44149999', '72150050', '72370000', '55333000', '06000000', '06593000', '88221000', '89889488', '84195000', '07889000', '07200000', '72000000', '12254320', '75619970', '88966300', '78232000', '06500000', '38425528', '89712060', '28946195', '89712054', '06886990', '89274005', '03280055', '38425385', '72370000', '72370000', '72370000', '72000000', '72370000', '72300000', '78232000', '72370000', '72370000', '72370330', '29683000', '72370000', '72370330', '72370000', '72370000', '72370000', '72209029', '72370000', '72600000', '72370000', '72370330', '72370000', '72370000', '72370000', '72370000', '72370000', '72370000', '72370000', '72370000', '72370000', '72370330', '72370000', '72370000', '72370330', '72370330', '72370000', '72370330', '72370000', '72370000', '72370000', '72370000', '72370000', '44149999', '43170000', '89712062', '76960970', '06850999', '44149999', '68605000', '44149999', '44149999', '44149999', '72000000', '01032041', '75602970', '44100000', '72000000', '72000000', '08700000', '87685000', '72000000', '44100000', '72300000', '72370000', '72000000', '72300090', '72000000', '72301012', '09616097', '72200000', '72000000', '72600000', '72000000', '75599970', '72000000', '72000000', '72000000', '72370000', '72200020', '72370000', '72370000', '72370000', '72370000', '72370000', '72370000', '89309405', '03108001', '84540000', '05350901', '05350901', '44149999', '72300000', '72000000', '72600970', '72000000', '72329278', '72000000', '72370000', '72000000', '56530000', '88551370', '72000000', '72000000', '72370000', '99999000', '76000000', '72370000', '72000000', '98664500', '72000000', '72000000', '17555550', '05350901', '72000000', '72000000', '72370210', '72000000', '72000000', '72000000', '72000000', '99151000', '78232000', '09817000', '33256000', '55300000', '75979970', '06950972', '38425467', '07780000', '78617000', '75669000', '72668490', '78232000', '99305000', '38514000', '89808505', '01419909', '89000000', '83033900', '89554222', '89707044', '81690901', '96810000', '78135610', '85666000', '89000000', '75900000', '89700083', '05423901', '05423905', '01009903', '00000000', '72600000', '86929000', '62841194', '28948129', '84100000', '78165900', '89961000', '08591200', '99973000', '75599970', '83823275', '89712050', '03711000', '44149999', '38425500', '89510000', '75939970', '75150000', '89510000', '78232000', '89712056', '04160325', '79672000', '38425566', '72230140', '07842010', '99780000', '07760000', '38480000', '75614970', '38480000', '38480000', '38480000', '67999999', '38480000', '38475000', '72000000', '38480000', '75664970', '75664970', '06262700', '89712084', '08888452', '25902016', '73300000', '67703020', '86846000', '78100000', '45833999', '07750000', '89655000', '06190097', '84154000', '34414580', '07824056', '02941010', '38480350', '07746120', '44149999', '06850000', '72370000', '72370000', '72370330', '38425477', '38425464', '38425455', '75262268', '75383129', '06803971', '75599970', '89409420', '44149999', '44100000', '72000000', '44149999', '72000000', '72000000', '72370127', '72901370', '72600000', '72000001', '84100000', '71600000', '89502930', '72000000', '72000000', '72300000', '72000000', '72370000', '72370000', '72000000', '72000000', '72000000', '72370000', '72000000', '72600000', '75924970', '72000000', '72970000', '72000000', '72000000', '72000000', '72000000', '88618000', '71950904', '72370000', '72370000', '72370000', '78232000', '72370000', '72370330', '72370000', '72000000', '72370330', '72370000', '72370000', '01000000', '72370000', '72370000', '72370000', '72370000', '99273010', '72370000', '72370000', '72370330', '72370000', '07290000', '89317000', '72370000', '72370000', '72330000', '69710000', '72600000', '72050010', '72000000', '72000000', '72370000', '99999000', '72370000', '72000000', '72000000', '72300000', '72370000', '99999000', '78283000', '78617000', '05913150', '75259970', '44149999', '72000000', '72000000', '72000000', '38814000', '76566000', '72000000', '72000000', '73300000', '72300000', '72000000', '72190000', '72370000', '72370310', '72370000', '72370000', '72000000', '72000000', '72000000', '95377410', '72902040', '07790000', '06876800', '99657000', '98908401', '78617000', '05001970', '89601230', '97787660', '45829004', '78165900', '34007970', '89800000', '82306100', '80125030', '82020000', '86000000', '79840640', '88330000', '82020000', '20211903', '05350901', '43330000', '75599970', '38480000', '75619970', '44149999', '44149999', '07780550', '44149999', '07400000', '84100000', '75599970', '05451900', '98790000', '78617000', '05350901', '89712072', '44149999', '04469010', '06899000', '99709910', '85969190', '38480000', '38480000', '09591108', '72305970', '38475000', '38480000', '38480000', '84195000', '89712226', '71608971', '88530366', '72360005', '72000000', '99110000', '04618916', '75619970', '18176170', '06850000', '89309630', '84148000', '72000000', '72370000', '72370000', '72370000', '75664000', '34413273', '06486120', '72000000', '85828000', '06750000', '76890970', '06950999', '93822086', '77654970', '73080000', '38425552', '05038050', '55300970', '06750000', '76492970', '44100000', '84100000', '72370000', '72000000', '84100000', '72305970', '72000000', '72000000', '72000000', '72520340', '76535764', '72000000', '72000000', '09700000', '75939970', '88560000', '72000000', '72000000', '72370330', '02523170', '44149999', '72200000', '72000000', '72300000', '72000000', '72370000', '32415207', '72305970', '72300000', '72328608', '71928120', '99702026', '09596567', '89869000', '78232000', '89689000', '99999000', '72370000', '72370210', '72370000', '72370090', '72000000', '72370000', '72370000', '72370230', '72370330', '72370000', '72370000', '72370000', '72370000', '72370000', '72370000', '72240090', '72370000', '72370000', '72370000', '72370000', '72370000', '71690000', '72370000', '72370000', '75599970', '72370000', '72370000', '72370000', '72370000', '72370330', '07231910', '89655000', '72370000', '72370000', '72370330', '72370000', '72370000', '07900000', '05350901', '04559909', '06266990', '71470000', '78232000', '72000000', '72000000', '72000000', '79888970', '72370000', '72000000', '72799999', '72190000', '72000000', '72000000', '89603190', '72000000', '72000000', '89659000', '72370330', '72370120', '72370000', '72370000', '72370290', '72370000', '71010970', '72600000', '72625305', '84100000', '72705970', '84100000', '72000000', '04852200', '67673108', '75391273', '38425450', '78100000', '58433100', '88667000']#, '28928668', '98790000', '06890999', '75800000', '89000000', '81207000', '89000000', '89000000', '01311936', '88900000', '01310915', '45710111', '89000000', '07700000', '79800001', '34410210', '14601210', '89598000', '34007970', '07800000', '44100000', '84154000', '44149999', '44100000', '75602970', '44100000', '07800000', '79870000', '08590922', '72970000', '38480000', '72600000', '05573900', '38480000', '71205000', '89625000', '89516000', '38480000', '38480000', '89712056', '72600970', '44149999', '72710000', '78165900', '86846000', '84540130', '75939970', '44149999', '75614970', '78165900', '44149999', '89712224', '38480000', '38480000', '38480000', '99100000', '79160040', '07760000', '86590000', '75599970', '09400000', '72000000', '06855999', '78100000', '72000000', '85552000', '72000000', '89712160', '06890970', '34887374', '72370000', '05526100', '72370000', '44149999', '38425427', '01043907', '04602904', '38425376', '71570900', '69710000', '99100000', '44100000', '73370000', '44149999', '06850000', '72000000', '72000000', '72000000', '72302260', '44100000', '72000390', '72225971', '72415000', '44149999', '72370000', '72000000', '72000000', '72000000', '85706000', '72000000', '75599970', '06850000', '67700000', '72000000', '04674901', '85552000', '72600000', '72000000', '72701300', '72000000', '72000000', '72000000', '71608900', '72669100', '72370330', '72601370', '72370000', '72370000', '72000000', '72370330', '72600000', '72375330', '72370330', '72370330', '72000000', '72370000', '78232000', '33405325', '72370330', '72370000', '72370000', '72400000', '72370000', '72370000', '72370000', '72370000', '72370000', '72370000', '72370000', '72370000', '72370000', '99999000', '85942200', '72370000', '72313790', '72300000', '72370330', '72370000', '72370000', '38480972', '02937202', '72000000', '72000000', '72000000', '72000000', '76960970', '72000000', '72370330', '72305970', '06850000', '75939970', '72000000', '72600000', '72000000', '72000000', '73300000', '71710000', '99310630', '72600000', '72000000', '72300000', '72000000', '72370000', '72370000', '72370000', '72370000', '56100000', '72000000', '72000000', '72000000', '72375290', '72600000', '07790001', '08331400', '37555000', '78232000', '85597000', '75939970', '89712050', '06836440', '79855000', '75392706', '75939970', '34415075', '38480970', '73105909', '99100000', '70070936', '24715090', '18270000', '89000000', '89000000', '08956000', '85989000', '75905900', '89803331', '38480000', '75599970', '37415435', '88690000', '89542000', '72903490', '07700000', '09297025', '85636000', '37415357', '38425428', '07809010', '78165900', '38425427', '75599970', '93805770', '73903190', '89598000', '44149999', '06318745', '38480000', '84100000', '38425588', '38480000', '38480000', '38480000', '78165900', '38425381', '75602970', '38475000', '72000000', '72000000', '44100000', '05001900', '89712114', '35179000', '89623000', '69710000', '72000000', '72370000', '06850000', '72370000', '72370330', '75664000', '75924625', '05361000', '89603050', '72300000', '72370310', '05868110', '07745504', '02523970', '72370090', '72000000', '07647080', '06816900', '89833000', '78232000', '86665000', '08915000', '78232000', '07750000', '38425426', '76419970', '38425496', '75599970', '06890992', '72580900', '44149999', '44149999', '72000000', '78232000', '78212560', '72000000', '72000000', '72200000', '72000000', '72000000', '75939970', '78100000', '72600000', '72370000', '34408000', '07796130', '72370000', '72370330', '72000000', '72000000', '72000000', '72415080', '72000000', '72000000', '72000000', '72000000', '72000000', '75939970', '75834970', '45100000', '06715999', '72370000', '71000000', '72370330', '72370330', '72330300', '72370330', '72300000', '72370000', '72370000', '72370000', '72370000', '72370000', '72370000', '72370000', '99100000', '72370000', '89556000', '72000000', '72330000', '72370330', '72370000', '72370000', '72370000', '05072901', '72370000', '72000000', '00729134', '72370000', '72370330', '72370000', '72370000', '72000000', '72370000', '72370000', '72370000', '72370000', '72370000', '72370330', '84680000', '72902260', '84100000', '75939970', '72000000', '72000000', '72000000', '72000000', '72000000', '72309220', '72000000', '75967150', '72000000', '78232000', '72000000', '72000000', '99100000', '72370000', '72370330', '72370330', '72300000', '72370000', '72000000', '72370330', '72000000', '72370000', '72370000', '72375150', '78617000', '72600000', '72000000', '72300000', '72600000', '72600000', '72000000', '85516000', '99100000', '89583000', '84100000', '06850000', '38480971', '38480000', '99802000', '75606651', '38425597', '89000000', '88742508', '99700970', '84000000', '89000000', '82500000', '75800000', '78800004', '75559970', '89000000', '88162243', '75664970', '88596000', '75979970', '09780900', '99100000', '47781900', '96936000', '44149999', '71000000', '89644000', '06850000', '07790000', '44149999', '44149999', '89510000', '78165900', '78617000', '07780000', '92920510', '85829000', '88985000', '72891000', '38480000', '78617000', '88560000', '38480000', '75664970', '03943100', '38475000', '38480000', '72300000', '84100000', '96116390', '96100000', '38480000', '07641000', '38480000', '89712058', '44100000', '89510000', '89510000', '38480000', '75614970', '75965000', '75939970', '36841227', '89625000', '84100000', '02951082', '07780000', '72300000', '38425588', '72000000', '99100000', '05338900', '67743250', '86500000', '72370000', '99100000', '72370000', '72370330', '72370000', '72370000', '33510630', '89712060', '38425627', '38480970', '69710000', '95685000', '44100000', '44100000', '72370000', '88584260', '00072000', '72000000', '44149999', '72000000', '72600000', '72000000', '72000000', '69710000', '69710000', '72000000', '72000000', '72000000', '72000000', '72000000', '72000000', '72000000', '72000000', '75619970', '72300000', '72000000', '72370000', '72000000', '72000000', '07200000', '72000000', '72000000', '72000000', '73206280', '72000000', '78232000', '05350901', '89877000', '85636000', '73070037', '72370330', '72370000', '72370000', '72600000', '72370000', '72000000', '72370000', '78232000', '72370000', '72370330', '07750000', '69710000', '72370000', '72000000', '69710000', '72370000', '72030000', '72601970', '72370330', '72370330', '07230597', '72370330', '72000000', '07961000', '38318000', '04614905', '07817170', '72465700', '72000000', '72000000', '72200000', '05350901', '85836000', '86603630', '72325418', '72000000', '72200000', '72000000', '72000000', '72000000', '72000000', '72370000', '78165900', '72370000', '72370000', '71805466', '72300000', '72000000', '72000000', '72370230', '72600000', '72370000', '89510000', '72000000', '72000000', '72000000', '72110000', '72000000', '06030999', '75919103', '88560000', '58404080', '73270900', '38425516', '75599970', '78617000', '34007970', '84100000', '89986000', '06190097', '78100000', '75939970', '84100000', '99594000', '72240050', '06338100', '29100904', '86000000', '20211903', '75800000', '89000000', '55612901', '89000000', '88162243', '07954000', '18270000', '95891000', '99708444', '89889000', '78617000', '44149999', '44149999', '06132190', '44149999', '44149999', '95902000', '06821035', '78100000', '06833190', '89510000', '89623000', '78232000', '86898000', '85970170', '88742508', '25931970', '89712054', '76664970', '71620300', '07700000', '07590000', '38425589', '19550000', '38425513', '38480000', '06890970', '06850000', '44100000', '44333000', '38480000', '78312120', '38480000', '72000000', '06980000', '38475000', '38475000', '38475000', '78165900', '38425472', '03874600', '07800000', '38480000', '89542000', '89712060', '73064202', '75954058', '79863270', '88560000', '06186797', '06650080', '44149999', '72000000', '72370000', '75599970', '08961000', '85970000', '88690000', '28401420', '06900070', '05480900', '06814250', '99973000', '99668000', '77654970', '72370000', '72370000', '72370000', '72370000', '72370330', '72104134', '72370330', '72370000', '72370330', '72370000', '72370310', '72370000', '72370000', '72370330', '72000000', '71700725', '55300000', '69710000', '72445970', '72000000', '44149999', '44149999', '06432230', '44149999', '72000000', '69710000', '72000000', '72000000', '72000000', '72326000', '72000000', '72000000', '89712210', '78100000', '89644000', '44100000', '44149999', '72301012', '71215902', '72301012', '06662760', '75834970', '72000000', '72370030', '75601970', '72000000', '72701301', '72160000', '07290097', '72000000', '07234320', '72000000', '72000000', '72000000', '72370000', '72370330', '72239205', '72370330', '72370000', '06650440', '72370000', '72370000', '72370330', '72370270', '72370000', '72370000', '05145901', '72370000', '78232000', '07914013', '06824360', '72370000', '72370000', '72370000', '72370000', '72000000', '72370000', '72370000', '72000000', '88331777', '72115952', '72370000', '75602970', '01221900', '84712590', '07809010', '04523912', '38480970', '72000000', '99100000', '85970000', '72906494', '86604380', '72045110', '72000000', '72000000', '88252230', '72300000', '72190000', '72000000', '72000000', '98469000', '07851970', '72000000', '72000000', '72300000', '72000000', '75834970', '72190000', '72000000', '75664970', '72370000', '72300000', '72000000', '72370000', '72370000', '72370000', '72370000', '18224230', '06850000', '72313619', '72000000', '72329311', '72000000', '72600000', '78232000', '72370000', '72928720', '07790000', '75599970', '78617000', '06886990', '75599970', '89523000', '72000000', '98790000', '72030100', '88362060', '85848000', '75939970', '88162243', '58404080', '89542000', '02522500', '99711400', '06886990', '89585000', '38480972', '38480000', '71950904', '88560000', '78100000', '34007970', '29731073', '34007970', '07750000', '89814400', '79501260', '75901970', '89000000', '72000000', '44149999', '38425588', '05865050', '72300000', '88151470', '44100000', '72000000', '86903670', '72000000', '75664970', '47408129', '72600970', '75599970', '75664970', '99915000', '05872030']
countCityNull = 0
countCityValid = 0
countExcept = 0
#update = open("update.sql","x")
for cep in ceps:
    try:
        address = get_address_from_cep(cep, webservice=WebService.VIACEP)
        if address['cidade'] != '':
            countCityValid += 1
            print("UPDATE PESSOAENDERECO pe SET pe.cd_municipio = (SELECT m.cd_municipio FROM MUNICIPIO m WHERE m.nm_municipio = '",address['cidade'],"') WHERE pe.nr_cep = '",cep,"';");
        else:
            countCityNull += 1
    except:
            countExcept += 1
print("countCityValid:",countCityValid)
print("countCityNull:",countCityNull)
print("countExcept:",countExcept)

hora_atual = datetime.now()
date_end = hora_atual.strftime('%H:%M:%S')
print("Iniciado em:",date_init)
print("Finalizado em:",date_end)


#cep = "50761425"
#endereco = pycep_correios.consultar_cep('37503130')
#print(cep+' '+endereco['cidade'])
