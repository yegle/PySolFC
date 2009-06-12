#!/usr/bin/env python
# -*- mode: python; coding: utf-8; -*-
##---------------------------------------------------------------------------##
##
## Copyright (C) 1998-2003 Markus Franz Xaver Johannes Oberhumer
## Copyright (C) 2003 Mt. Hood Playing Card Co.
## Copyright (C) 2005-2009 Skomoroh
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
##---------------------------------------------------------------------------##

# This layouts converted from Kyodai Mahjongg game
# http://www.kyodai.com/index.en.html
# http://files.cyna.net/layouts.zip

from mahjongg import r

# /***********************************************************************
# // game definitions
# ************************************************************************/

#
r(5200, "Another Round", ncards=140, layout="0aagaaihbhacfachacjhdghdiaecaeeaegoehaeiaekaemhfdhffhfhhfjhflagaagcageogeaggoggagiogiagkogkagmagohhbhhdhhfhhhhhjhhlhhnaiaaicoicaieoieaigoigaiioiiaikoikaimoimaiohjbhjdhjfhjhhjjhjlhjnakaakcakeakgakiakkakmakoamaamcammamoaoaaocaoeaogaoiaokaomaoohpbhpdhpfhphhpjhplhpnaqaaqcoqcaqeoqeaqgoqgaqioqiaqkoqkaqmoqmaqohrbhrdhrfhrhhrjhrlhrnasaascaseoseasgosgasiosiaskoskasmasohtdhtfhthhtjhtlaucaueaugouhauiaukaumhvghviawfawhawjhxhaygayi")
r(5201, "Aqab's", layout="0caedagcaicccbcgcckceabegcembggahdahjbigbkabkeckgbkibkmbmabmccmedmgcmibmkbmmboacocdoedogdoicokbombqabqccqedqgcqibqkbqmbsabsecsgbsibsmbugawdbwgawjcyabygcymcAcbAgcAkcCedCgcCi")
#
r(5202, "Big Mountain", layout="0aaaaaqaeihfiaghogiagjhhhvhihhjaigoihaiiCiioijaikhjgvjhhjivjjhjkakfokgakhCkhokiakjCkjokkaklhlfvlghlhvlihljvlkhllameomfamgomhCmhamiomjCmjamkomlammhnehngvnghnivnihnkvnkhnmaodaofoofaohoohCohaojoojCojaoloolaonhpehpgvpghpivpihpkvpkhpmaqdaqfoqfaqhoqhCqhaqjoqjCqjaqloqlaqnhrehrgvrghrivrihrkvrkhrmaseosfasgoshCshasiosjCsjaskoslasmhtfvtghthvtihtjvtkhtlaufougauhCuhouiaujCujoukaulhvgvvhhvivvjhvkawgowhawiCwiowjawkhxhvxihxjayhoyiayjhziaAiaGaaGq")
#
r(5203, "Bridge", layout="0aaaaacaaeaagaaihbahbchbehbghbiocaoccoceocgociwdavdcvdevdgwdioeboedoefoehvfahfcvfchfevfehfgvfgvfiogbagdogdagfogfoghvhahhcvhchhevhehhgvhgvhioibaidoidaifoifoihvjahjcvjchjevjehjgvjgvjiokbokdokfokhvlavlcvlevlgvliCmaCmivnavncvnevngvniooboodoofoohvpahpcvpchpevpehpgvpgvpioqbaqdoqdaqfoqfoqhvrahrcvrchrevrehrgvrgvriosbasdosdasfosfoshvtahtcvtchtevtehtgvtgvtiouboudoufouhwvavvcvvevvgwviowaowcoweowgowihxahxchxehxghxiayaaycayeaygayi")
r(5204, "Butterfly 2", layout="0aaeaagabcabiadbadjhefvefaenafaafeofeafgofgaflafphgdvgdwgfhghvghahaaheoheahgohgahkahqhifvifcinbjbbjjajqblcbliblqbmocndcnhcnmapbbpdapfbphapjbplapnhqbpqdiqfpqhiqjpqlhqnarbbrdarfbrharjbrlarnctdcthctmbuobvcbvibvqbxbbxjaxqhyfvyfcynazaazeozeazgozgazkazqhAdvAdwAfhAhvAhaBaaBeoBeaBgoBgaBlaBphCfvCfaCnaDbaDjaFcaFiaGeaGg")
r(5205, "ChessMania", layout="0aaaaacaaeaagaajaalaanaapacaacgbcmaeaaegaejaelaenaepaibbidaifbihaijbilainbipbkbakdbkfakhbkjaklbknakpambbmdamfbmhamjbmlamnbmponfonhonjonlbobaodbofaohbojaolbonaopopfppioplaqbbqdaqfbqhaqjbqlaqnbqporforlbsbasdbsfashbsjaslbsnaspaubbudaufbuhaujbulaunbupbwbawdbwfawhbwjawlbwnawpaBaaBcaBgaBjaBlaBpaDabDdaDgaDjbDmaDpaFaaFeaFgaFjaFnaFp")
r(5206, "Cross", layout="0baebagbaiaccdcebcgdciackaeacecdeebegdeicekaemcgadgcdgebggdgidgkcgmbiabicaiebigaiibikbimbkabkcakebkgakibkkbkmcmadmcdmebmgdmidmkcmmaoacocdoebogdoicokaomaqcdqebqgdqiaqkbsebsgbsi")
r(5207, "Cupido's Heart", layout="0aadaalbbfbbjcchaddadlbefcehbejcghdhfdidcihdjbdjjckhdkldlacmhdmndnbdodcohdopeqedqqdsddspdtbdundvadwldxbdxjdyddyhdzfcAhaCecChaCkbEfcEhbEjcGh")
r(5208, "Diamond", ncards=140, layout="0aaiaakacgbcibckacmaeebegceicekbemaeoagcbgecggdgidgkcgmbgoagqaiabicciedigeiieikdimciobiqaisakabkcckedkgekiekkdkmckobkqaksamcbmecmgdmidmkcmmbmoamqaoebogcoicokbomaooaqgbqibqkaqmasiask")
r(5209, "Dragon 2", layout="0bafbbdobeobgbbhbcfbcmbdkodlodnbdobecaegbemofcbgabgcbghbgjaglohavhbohcbiabicbijbilojbbjhojjojlbkbbkfokhbkjvkjbklvklolbolfblholjollbmbcmdbmfbmjbmlboioojbokaoohpobqhbqjaqobrforhorjasdosfbshvshbsjvsjbslbsnhtdbtfothotjaubaudbuhbujbwgbwkbwmbydoyebyfbymayohzobAcaAobBjbCdoCebCfoCgbCh")
r(5210, "Empty Pyramids", layout="0aaiabghbiabkaccacehcgocihckacmacoadghdiadkaeiahiaighiiaikajehjgojihjkajmakchkeokgvkiokkhkmakoalahlcolevlgClivlkolmhloalqhmaamchmeomgvmiomkhmmamohmqonahncanehngonihnkanmhnoonqvoaoochoeaoghoiaokhomooovoqCpavpcopehpgapiopihpkopmvpoCpqvqaoqchqeaqghqiaqkhqmoqovqqorahrcarehrgorihrkarmhroorqhsaaschseosgvsioskhsmasohsqatahtcotevtgCtivtkotmhtoatqauchueougvuioukhumauoavehvgovihvkavmawghwiawkaxiaAiaBghBiaBkaCcaCehCgoCihCkaCmaCoaDghDiaDkaEi")
r(5211, "Fish face", layout="0bajbciocjbckvdjbehoeibejoekbelcggcgmchichkcifcincjhcjlckebkjckoclgclmcmebmiomjbmkcmocnccnqcoeboioojbokcoobpbcpgcpmbprcqebqjcqoaracrhcrlarsbsfbsnbtiotjbtkbugbumbwhbwlbyibykcAjcBhcBlbDgbDmaFfaFn")
r(5212, "Floating City", layout="0oagoaiocdocfochocjoclocphdahdchdmhdoaeboebaedaefaehaejaelaenoenhfahfcvfchfmvfmhfoagbagnahdvheahfahhahjvhkahlaibainvjgvjiakbCkhaknhlfhlhhljambamdamfomgamhCmhomiamjamlamnomphnfhnhhnjjoaaobCobaodCodaofCofoogaohCohooiaojCojaolColaonConjooCopooqhpfhphhpjaqbaqdaqfoqgaqhCqhoqiaqjaqlaqnoqphrfhrhhrjasbCshasnvtgvtiaubaunavdvveavfavhavjvvkavlawbawnhxahxcvxchxmvxmhxoayboybaydayfayhayjaylaynoynhzahzchzmhzooAdoAfoAhoAjoAloApoCgoCi")
#r(5213, "Flowers 2", layout="0aaiacgbciackadcadoaeiafabfcafeafmbfoafqahcahoaihaijhjiakfakhakjaklhlghlihlkamdamfamhomhamjomjamlamnhnehnghnivnihnkhnmaobaodaofoofaohoohaojoojaoloolaonaophpchpehpgvpghpivpihpkvpkhpmhpoaqbaqdoqdaqfoqfaqhoqhCqhaqjoqjCqjaqloqlaqnoqnaqphrchrehrgvrghrivrihrkvrkhrmhroasbasdasfosfashoshasjosjasloslasnasphtehtghtivtihtkhtmaudaufauhouhaujoujaulaunhvghvihvkawfawhawjawlhxiayhayjazcazoaBabBcaBeaBmbBoaBqaCiaDcaDoaEgbEiaEkaGi")
#r(5214, "Full Vision 3", layout="0aaeaagaaihbehbiacbhccacdacfhcgachacjhckaclacnhcoacpaeahebaecaeeaegaeiaekhelaemagbhgcagdagfhggaghagjhgkaglagnhgoagphhehhiaieaigaiiainhioaiphjgakeakgakiaknhkoakphlehliambhmcamdamfhmgamhamjhmkamlamnhmoampaoahobaocaoehofaogaoiaokholaomaqbhqcaqdaqfhqgaqhaqjhqkaqlaqnhqoaqphrehriaseasgasiasnhsoasphtgaueaugauiaunhuoauphvehviawbhwcawdawfhwgawhawjhwkawlawnhwoawpayahybaycayeaygayiaykhylaymaAbhAcaAdaAfhAgaAhaAjhAkaAlaAnhAoaAphBehBiaCeaCgaCi")
r(5215, "Hidden Words", layout="0haahachaehaghalabaabcobdabeabgabjablbbnabphcahcchceocghchhckhcqadgadmodohefheihemheoafgafjofjaflafnafphgfogghgkhgmhgohichiehikhinajaojaajcojdajeajghjhajjajlajnajphkbhkfokjhklhkpalaalghlialjalmombhmchmehmnanaancanebnganjanlannbnphochoiholhqchqfhqihqkaraarcarearjhschshhslhsnhspatgatjatlatnatphuchuhhunavaavcaveavjhvkhwdhwfhxihxmhxqayahybaycayeaygayjaylaynhyoayphzfhzkaAabAdaAghAhaAjaAmaAphBlhBnhBqaCahCbaCghCiaCjaCphDfhDp")
r(5216, "Hovercraft", layout="0aadaafaahaajjbgdccdceacgdcidckjdgaedaefaehaejhfgagfpggaghhhgaigajajjgajmhkaakghkmalaolaalmolmhmavmaemghmmvmmanaonaCnaenceneenienkanmonmCnmhoavoaeoghomvomapaopaapmopmhqaaqghqmarajrgarmasghtgaufpugauhhvgawdawfawhawjjxgdycdyeaygdyidykjzgaAdaAfaAhaAj")
r(5217, "Hurdles", layout="0aaaaacaaeaagaaiaakaamaaohbahbchbehbghbihbkhbmhboacaocaaccoccaceoceacgocgaciociackockacmocmacoocohdahdchdehdghdihdkhdmhdoaeaaecaeeaegaeiaekaemaeoagaagcageaggagiagkagmagohhahhchhehhghhihhkhhmhhoaiaoiaaicoicaieoieaigoigaiioiiaikoikaimoimaiooiohjahjchjehjghjihjkhjmhjoakaakcakeakgakiakkakmakoamaamcameamgamiamkammamohnahnchnehnghnihnkhnmhnoaoaooaaocoocaoeooeaogoogaoiooiaokookaomoomaooooohpahpchpehpghpihpkhpmhpoaqaaqcaqeaqgaqiaqkaqmaqo")
r(5218, "Tornado", layout="0babaadaambaoabibegbekofdbfeoffafiofioflbfmofnbgchgibgoahaahiohiahqhibhiihipajbajeijfajgvjgajiojiajkvjkijlajmajphkbhkihkpalcalialohmchmoandineanfanianlinmannapbipdapevpeipfapgapkiplapmvpmipnappardirearfariarlirmarnhschsoatcatiatohubhuihupavbaveivfavgvvgavioviavkvvkivlavmavphwbhwihwpaxaaxioxiaxqbychyibyoozdbzeozfazioziozlbzmoznbAgbAkaDibEbaEdaEmbEo")
#
r(5219, "IloveU", layout="0caddafcahdaldandapdcbcciceacejcgacgkdibcilckdckmcmecmndngdnpcoeconcqdcqmdsbcslcuacukcwacwjdybcyidzldzndzpcAddAfcAhdBpdDldDndDp")
r(5220, "Inazuma", layout="0caaaaocaqcccacmccoacqceebeiaekcemaeoagacggcgkagmciaaicciibimakackcakeckkamccmeamgcmmaoecogaoicoocqaaqgdqiaqkcqqcscasicskasmcueaukcumauocwgawmcwoawqbyecyiayocyqaAecAgcAkaAqaCccCeaCgbCicCmaEacEcaEecEocGaaGccGq")
r(5221, "JPs", layout="0baabakbbmbcabckbcobdmbdqbeabeobfqbgabhobhqbiabicbiebigbiibikbimbjobkabkcbkebkgbkibkkbkmamqbqabqcbqebqgbqibqkbqmbqobqqbsabscbsebsgbsibskbsmbsobsqbuabuhbujbwabwhbwjaxqbyabyhbyjbAabAcbAgbAibCabCcbCebCgbCibEabEcbEebEgbEibGe")
r(5222, "Japan", ncards=96, layout="0baabacbaebagbaibcaacebcibeaaeebeibgabgcbgebggbgiahoajkajoalgalialkhllalmaloangbnibnkanmapebpgbpiapkapmbrebrgariarkatehtfatgatiavaavcavebwibwoaxaaxcbxmbyiaykazabAgbAibAkbAmbAobCiaCkbDmbEibEo")
r(5223, "Krebs", layout="0aaaaacaaeaagbaibalaanaapaaraatacaactaeaaetagaagtaiaCikaitvjkakaCkjokkCklaktvljhlkvllamaCmiomjamkCmkomlCmmamtvnihnjvnkhnlvnmaoaCohooiaojCojookaolColoomConaotvphhpivpjhpkvplhpmvpnbqaCqgoqhaqiCqioqjaqkCqkoqlaqmCqmoqnCqobqtvrhhrivrjhrkvrlhrmvrnCshosiasjCsjoskaslCslosmCsnbtavtihtjvtkhtlvtmbttCuioujaukCukoulCumavavvjhvkvvlavtCwjowkCwlaxavxkaxtCykazaaztaBaaBtaDaaDtaFaaFtaHaaHcaHeaHgdHidHlaHnaHpaHraHt")
r(5224, "Kumo", layout="0caadaccaecagbaibamdaqdcacccacebcgbckdcoceaaecceebeidembeqcgabgccggdgkbgobiabiediibimbiqbkcdkgckkbkockqbmadmebmicmmamocmqdocbogbokaomcoodoqdqabqebqicqkcqmdqocqq")
r(5225, "Kyodai 14", layout="0aaiachhciacjodiaefhegaehheiveiaejhekaelofhCfiofjagchgdagehgfagghghagivgihgjagkhglagmhgnagoohiaibhicaidaihhiiaijainhioaipakcbkgokhbkivkiokjbkkakohlchloamcbmfbmlamoaoahobaochodaoeooehofvofaogooghohvohaoiooihojvojaokookholvolaomoomhonaoohopaoqaqcbqfbqlaqohrchroascbsgoshbsivsiosjbskasoaubhucaudauhhuiaujaunhuoaupoviawchwdawehwfawghwhawivwihwjawkhwlawmhwnawooxhCxioxjayfhygayhhyivyiayjhykayloziaAhhAiaAjaCi")
r(5226, "Kyodai 17", layout="0daacaccaecagcaicakdamccaccgccmceacegcemcgacgccgecggcgicgkcgmciadigcimckadkgckmcmacmccmecmgcmicmkcmmcoacogcomcqacqgcqmdsacsccsecsgcsicskdsm")
#
r(5227, "Kyodai 18", layout="0daidchdcjdegdekdgfdgldiedimdkdakidkndmcamhamjdmodobaogaoiaokdopdqaaqfaqhaqjaqldqqdsbasgasiaskdspducauhaujduodwdawidwndyedymdAfdAldCgdCkdEhdEjdGi")
r(5228, "Kyodai 20", layout="0aaeaagaaiaakaamaaohbjacdaciackacpaecbehbelaeqagbaggagmagraiaaifhigaihoihhiiviiaijoijCijhikvikailoilhimainaisakaakebkjakoaksamaamdcmhamjcmlampamsaoahobaocoochodvodaoeooeCoehofvofaogooghohaoikojaokholaomoomhonvonaoooooCoohopvopaoqooqhoraosaqaaqdcqhaqjcqlaqpaqsasaasebsjasoassauaaufhugauhouhhuivuiaujoujCujhukvukauloulhumaunausawbawgawmawraycbyhbylayqaAdaAiaAkaAphBjaCeaCgaCiaCkaCmaCo")
#
r(5229, "Kyodai 23", layout="0aaehbeacdoceacfhdevdeaecaeeoeeaeghfdvfehffagaagcageogeaggagihhbhhdhhfhhhaiaaicoicaieoieaigoigaiihjbhjdvjdhjfvjfhjhakaakcokcakeokeCkeakgokgakihlbhldvldhlfvlfhlhamaamcomcameomeamgomgamihnbhndhnfhnhaoaaocaoeooeaogaoihpdhpfaqaaqcaqeoqeaqgaqihrbhrdhrfhrhasaascoscaseoseasgosgasihtbhtdvtdhtfvtfhthauaaucoucaueoueCueaugougauihvbhvdvvdhvfvvfhvhawaawcowcaweoweawgowgawihxbhxdhxfhxhayaaycayeoyeaygayihzdvzehzfaAcaAeoAeaAghBevBeaCdoCeaCfhDeaEe")
#
r(5230, "Kyodai 24", layout="0aaaiabaacaaejafaagaaiiajaakvbcibdCbfibhvbiacaicbaccacevceicfacgvcgaciicjackvdciddCddCdfidhCdhvdiaeaiebaecaeeveeiefaegvegaeiiejaekvfcifdCfdifhCfhvfiagaigbagcagevgeigfaggvggagiigjagkvhcihdChdihhChhvhiaiaiibaicaievieiifaigvigaiiiijaikvjcijdCjdCjfijhCjhvjiakaikbakcakevkeikfakgvkgakiikjakkvlcildClfilhvliamaimbamcamejmfamgamiimjamk")
r(5231, "Kyodai 25", layout="0cagbaicakbcgbckodgodkbegbekcggcgkbieoifbigciibikoilbimbkiolicmabmicmqboabogdoibokboqcqabqcoqdbqedqgdqkbqmoqnbqocqqbsabsgdsibskbsqcuabuicuqovibwibyeoyfbygcyibykoylbymcAgcAkbCgbCkoDgoDkbEgbEkcGgbGicGk")
#
r(5232, "Kyodai 26", layout="0aahhbhacgacihdghdiaefaehaejhffhfhhfjageaggagiagkhhehhghhihhkaidaifaihaijailhjdhjhhjlakcakeakgakiakkakmhlchlehlghlihlkhlmambamdamfamhamjamlamnhnbhnfhnhhnjhnnaoaaocaoeaogaoiaokaomaoohpahpchpehpghpihpkhpmhpoaqaaqcaqeaqgaqiaqkaqmaqohrahrchrehrghrihrkhrmhroasaascaseasgasiaskasmasohtbhtfhthhtjhtnaubaudaufauhaujaulaunhvchvehvghvihvkhvmawcaweawgawiawkawmhxdhxhhxlaydayfayhayjaylhzehzghzihzkaAeaAgaAiaAkhBfhBhhBjaCfaChaCjhDghDiaEgaEihFhaGh")
#
r(5233, "Kyodai 27", layout="0aagacfhcgachaeehefaegoeghehaeivfgagdhgeagfogfhggCggaghoghhgiagjvhfvhhaichidaieoiehifCifaigoighihCihaiioiihijaikvjevjgvjiakbhkcakdokdhkeCkeakfokfhkgCkgakhokhhkiCkiakjokjhkkaklvldvlfvlhvljamahmbamcomchmdameomehmfCmfamgomghmhCmhamiomihmjamkomkhmlammvndvnfvnhvnjaobhocaodoodhoeCoeaofoofhogCogaohoohhoiCoiaojoojhokaolvpevpgvpiaqchqdaqeoqehqfCqfaqgoqghqhCqhaqioqihqjaqkvrfvrhasdhseasfosfhsgCsgashoshhsiasjvtgauehufaugoughuhauiawfhwgawhayg")
#
r(5234, "Kyodai 28", layout="0baibbgbbkbcebcibcmbdcbdobeabeibeqbgacggvghcgiCgivgjcgkbgqbiacifciicilbiqbkackeakhakjckmbkqhlhhljbmacmdamgamiomiamkcmnbmqhnhhnjboacoeaohaojcomboqbqacqfcqicqlbqqbsacsgvshcsiCsivsjcskbsqbuabuibuqbvcbvobwebwibwmbxgbxkbyi")
#
r(5235, "Kyodai 41", layout="0CaeCagCaivbevbgvbiCcdoceocgociCcjvddhdevdfhdgCdgvdhhdivdjCecaeeoeeCeeaegoegaeioeiCeiCekCfavfbofchfdvfdhffvffCfghfhvfhhfjvfjofkvflCfmCgdageogeaggoggagiogiCgjChavhbohchhdvhdhhfvhfChghhhvhhhhjvhjohkvhlChmCicaieoieCieaigoigaiioiiCiiCikCjavjbojchjdvjdhjfvjfCjghjhvjhhjjvjjojkvjlCjmCkdakeokeakgokgakiokiCkjClavlbolchldvldhlfvlfClghlhvlhhljvljolkvllClmCmcameomeCmeamgomgamiomiCmiCmkvndhnevnfhngCngvnhhnivnjCodooeoogooiCojvpevpgvpiCqeCqgCqi")
#
r(5236, "Kyodai 42", layout="0oaboadCagoajoalhbahbcvbchbeobfvbgobhhbihbkvbkhbmacbacdacjaclhdbhddodevdfCdgvdhodihdjhdlaecaekhfchfeoffvfgofhhfihfkagdCggagjhhdhhfhhhhhjaieaiihjehjghjiakfCkgakhhlfvlghlhCmfamgomgCmhhnfvnghnhaogCoghpfhphCqcvqdoqeCqeaqgoqgoqiCqivqjCqkhrfhrhasgCsghtfvtghthCufaugougCuhhvfvvghvhawfCwgawhhxehxghxiayeayihzdhzfhzhhzjaAdCAgaAjhBchBeoBfvBgoBhhBihBkaCcaCkhDbhDdoDevDfCDgvDhoDihDjhDlaEbaEdaEjaElhFahFcvFchFeoFfvFgoFhhFihFkvFkhFmoGboGdCGgoGjoGl")
r(5237, "Lattice", layout="0aaiacebciacmaecbeeaegbeiaekbemaeoagecgiagmaicbieaigciiaikbimaioakeckiakmamcbmebmgdmibmkbmmamoboeeoibomaqabqccqeeqgdqieqkcqmbqoaqqbseesibsmaucbuebugduibukbumauoawecwiawmaycbyeaygcyiaykbymayoaAecAiaAmaCcbCeaCgbCiaCkbCmaCoaEebEiaEmaGi")
#
#r(5238, "Leo", layout="0aapabiablhbphcfacghchhclacnocpadjodladpvdpheeaefheiaelvelhepCepofihflCflafnofphgdagevgiagjoglagpvgphhiChiahlvhlhhpChphicaidoiihilCilainoipvjiajjojlajpvjpbkabkchkiCkiaklvklhkpCkpolbolihllalnolpbmabmcvmiamjomlampvmphnianlhnpooiholaonoophpfaphapjappaqfhqiaqlhqphrdarnasehsqhtcatpaudbumhuphvbcvgavqawccwlhwqhxbcxjaxpayccylhyphzbczgazqaAdbAmhAqhBcaBpaCehCphDeaDgaDohEgaEiaEmhEohFiaFkhFmhGk")
#
r(5239, "Loose Ends", layout="0aaaoabaaioapaaqhbahbihbqacboccachociacjocoacphdbhdivdihdpaecoedaegaeioeiaekoenaeohfchfivfihfoagdogeaghogiagjogmagnhhdhhivhihhnaieoifaiioiioilaimhjfhjihjlakgokgakiakkokkhlholihljamahmbamcomchmdvmdameomehmfvmfamgvmhamiCmivmjamkhmlvmlammommhmnvmnamoomohmpamqhnhonihnjaogoogaoiaokookhpfhpihplaqeoqfaqioqioqlaqmhrdhrivrihrnasdoseashosiasjosmasnhtchtivtihtoaucoudaugauiouiaukounauohvbhvivvihvpawbowcawhowiawjowoawphxahxihxqayaoybayioypayq")
r(5240, "Mini Traditional", ncards=48, layout="0aaeacdacfhdeaecaeeoeeaeghfdvfehffagbagdogeagfaghhhchhevhehhgaiaaicoicaieoieaigoigaiihjchjevjehjgakbakdokeakfakhhldvlehlfamcameomeamghneaodaofaqe")
r(5241, "Mini-Layout", ncards=8, layout="0aabaadacahcbhcdaceaebaed")
r(5242, "Mission Impossible", layout="0baabamaapccaccmacpdeacecbeeaegbeicekdemaepcgacgmagpbiabimaipakpbmacmcdmeemgdmicmkbmmampcocaopdqeaqpcscaspbuacucdueeugduicukbumaupawpbyabycbyebygbyibykbymaypcAacAgaApdCadCgaCpeEaaEp")
#
r(5243, "Multi X", layout="0aaaaaiaaqhbbhbhhbjhbpoccocgockocovddvdfvdlvdnceeCeecemCemvfdvffvflvfnogcoggogkogohhbhhhhhjhhpaiaaiiaiqhjbojcvjdCjevjfojghjhojihjjojkvjlCjmvjnojohjpakaakiakqhlbhlhhljhlpomcomgomkomovndvnfvnlvnncoeCoecomComvpdvpfvplvpnoqcoqgoqkoqohrbhrhhrjhrpasaasiasqhtbotcvtdCtevtfotghthotihtjotkvtlCtmvtnotohtpauaauiauqhvbhvhhvjhvpowcowgowkowovxdvxfvxlvxncyeCyecymCymvzdvzfvzlvznoAcoAgoAkoAohBbhBhhBjhBpaCaaCiaCq")
#r(5244, "New Layout 2", layout="0CabCadCafacapcahccvccacepcehcgvcgheaveaaecpecheeveeaegpegCfaCfcCfeCfgagapgahgcvgcagepgehggvggChaChcCheChghiaviaaicpichievieaigpigakaqkahkcwkcakeqkehkgwkghmawmaamcqmchmewmeamgqmgaoaqoahocwocaoeqoehogwoghqavqaaqcpqchqevqeaqgpqgCraCrcCreCrgasapsahscvscasepsehsgvsgCtaCtcCteCtghuavuaaucpuchuevueaugpugawapwahwcvwcawepwehwgvwgCybCydCyf")
r(5245, "Okie's Nitemare", layout="0aaoaaqbbeabmhbpacoacqcddbdgadmhdpaeoaeqbfccffafmhfpagoagqbhehhpaiiaioaiqhjihjqakiakqalohlqammhmoamqandankhnmanoonohnqaobaoihokaompomhooaoqapghpiapkopkhpmapoopohpqaqabqcoqdbqeoqfhqgaqioqihqkvqkCqlaqmpqmhqoaqqarghriarkorkhrmaroorohrqasbasihskasmpsmhsoasqatdatkhtmatootohtqaumhuoauqavohvqawiawqhxihxqbyeayiayoayqhzpbAccAfaAoaAqaBmhBpcCdbCgaCoaCqaDmhDpbEeaEoaEqaFmhFpaGoaGq")
r(5246, "Orbital", ncards=84, layout="0dafdahdajdchcehbghbihbkhclablfbljclocnabncbnebnkbnmcnocpabpfbpjcpobqhbshbuhcwhdyhdAfdAhdAj")
r(5247, "Owl", layout="0baebagbaibakbambcdbcncecbejbeocgbbghcgjbglbgpcicbijbiobkdbknclablpbmebmmcnbanpcodaofbohbojbolbonhopipfappoppcqdaqfbqhbqjbqlbqnhqpcrbarpbsebsmctabtpbudbuncwcbwjbwocybbyhcyjbylbypcAcbAjbAobCdbCnbEebEgbEibEkbEm")
r(5248, "Pantheon", layout="0baebcebdgbdqbeeaeiaekaemaeobfcbfgbfqbgebhcbiebjcojdbjgbjqbkabkeakiakkakmakoolbblcoldblgblqbmabmeonbbncboaoodboeopbbpcbpgbpqbqabqeaqiaqkaqmaqoorbbrcbrgbrqbsaosdbseotbbtcbuabueovbbvcovdbvgbvqbwabweawiawkawmawobxcoxdbxgbxqbyebzcbAebBcbBgbBqbCeaCiaCkaCmaCobDgbDqbEebGe")
#
r(5249, "Papillon", layout="0bagbaibakobhobjbcfbchbcjbclodhodjbecbeebegbeibekbembeoofdofnbgdbgnbiebimojeojmbkdbkfbklbknbmcbmgbmkbmobobbohbojbopopibqabqibqqoribsbbshbsjbspbucbugbukbuobwdbwfbwlbwnoxeoxmbyebymbAdbAnoBdoBnbCcbCebCgbCibCkbCmbCooDhoDjbEfbEhbEjbEloFhoFjbGgbGibGk")
r(5250, "Pyramid 1", layout="0aagaaiaceacghchaciackaecbeebegbeibekaemagabgcbgecggcgibgkbgmagoaiabicciecigvihciicikbimaioakabkcckedkgdkickkbkmakoamabmccmedmgdmicmkbmmamoaoaboccoecogvohcoicokbomaooaqabqcbqecqgcqibqkbqmaqoascbsebsgbsibskasmaueaughuhauiaukawgawi")
r(5251, "Pyramid 2", layout="0aaeaagaaiaccbcebcgbciackaeabecbeeoefbegoehbeibekaemagacgcdgedggdgicgkagmbiadiceieeigeiidikbimbkadkcekeekgekidkkbkmamacmcdmedmgdmicmkammaoabocboeoofbogoohboibokaomaqcbqebqgbqiaqkaseasgasi")
#
r(5252, "Quad", layout="0baabacbaeaagbaibakbamobbobdobjoblbcabccvccbceacgbcibckvckbcmodboddodjodlbeabecvecbeeaegbeibekvekbemofbofdofjoflbgabgcbgeaggbgibgkbgmaiaaicaiebigaiiaikaimbkabkcbkeakgbkibkkbkmolboldoljollbmabmcvmcbmeamgbmibmkvmkbmmonbondonjonlboabocvocboeaogboibokvokbomopbopdopjoplbqabqcbqeaqgbqibqkbqm")
#
r(5253, "Rectangle", layout="0daadacdaedagdcadccdcedcgdeadecdeedegdgadgcdgedggdiadicdiedigdkadkcdkedkgdmadmcdmedmgdoadocdoedogdqadqcdqedqg")
r(5254, "Reindeer", ncards=64, layout="0haeabdocchdbadnaecheehemaffaflafohgkahfahhahjajfajjalfalhaljallhmmanfanjonnaooapfaphapjarfarjaslatfathatjhtmouahufounhvbhvjavoawchwfawkhxdaxghxhhxlayioymazevznaAiaBchBdaBgaBohCbhChaCioDaoDivEh")
r(5255, "Rings", layout="0aahabfhbhabjacdhcfachochhcjaclhddadfodfhdhvdhadjodjhdlaebaedhefaehoehhejaelaenhfcaffhfhafjhfmagcaghagmhhchhmaicaihaimhjcajfhjhajjhjmakbakdhkfakhokhhkjaklaknhldalfolfhlhvlhaljoljhllamdhmfamhomhhmjamlanfhnhanjaoaaohaooaqaaqhaqoarfhrharjasdhsfashoshhsjaslhtdatfotfhthvthatjotjhtlaubaudhufauhouhhujaulaunhvcavfhvhavjhvmawcawhawmhxchxmaycayhaymhzcazfhzhazjhzmaAbaAdhAfaAhoAhhAjaAlaAnhBdaBfoBfhBhvBhaBjoBjhBlaCdhCfaChoChhCjaClaDfhDhaDjaEh")
r(5256, "River Bridge", ncards=116, layout="0aafaalacfachacjaclhdfhdhhdjhdloefoehoejoelvffvfloggogiogkvhfhhhhhjvhloigaiioiioikvjfhjhhjjvjlajoakcokgakiokiokkakmakqalavlfhlhhljvllomgamiomiomkvnfhnhhnjvnloogaoiooiookvpfhphhpjvploqgaqioqioqkvrfhrhhrjvrlosgasiosioskvtfhthhtjvtlaucougauiouioukauoavavvfhvhhvjvvlavmavqowgawiowiowkvxfhxhhxjvxloygoyioykvzfvzloAfoAhoAjoAlhBfhBhhBjhBlaCfaChaCjaClaEfaEl")
#
r(5257, "Roman Arena", layout="0CaaCacCaeCagCaivbbvbdvbfvbhCcaoccoceocgCcivdbhddadehdfvdhCeaoecoegCeivfbhfdafehffvfhCgaogcoggCgivhbhhdahehhfvhhCiaoicoigCiivjbhjdajehjfvjhCkaokcokgCkivlbhldalehlfvlhCmaomcCmcCmeomgCmgCmivnbhndvndanehnfvnfvnhCoaoocooeCoeoogCoivpbhpdvpdapehpfvpfvphCqaoqcCqcCqeoqgCqgCqivrbhrdarehrfvrhCsaoscosgCsivtbhtdatehtfvthCuaoucougCuivvbhvdavehvfvvhCwaowcowgCwivxbhxdaxehxfvxhCyaoycoygCyivzbhzdazehzfvzhCAaoAcoAeoAgCAivBbvBdvBfvBhCCaCCcCCeCCgCCi")
r(5258, "Rugby", layout="0aafaahaceacgaciaecaeeaegaeiaekagaagcagehgfagghghagiagkagmaiaaichidaiehifaighihaiihijaikaimakahkbakchkdakeikfakgikhakihkjakkhklakmamahmbamchmdameimfamgvmgimhamihmjamkhmlammondonjaoahobaochodaoevoeiofaogvogiohaoivoihojaokholaomopdopjaqahqbaqchqdaqeiqfaqgvqgiqhaqihqjaqkhqlaqmasahsbaschsdaseisfasgishasihsjaskhslasmauaauchudauehufaughuhauihujaukaumawaawcawehwfawghwhawiawkawmaycayeaygayiaykaAeaAgaAiaCfaCh")
r(5259, "Shapeshifter", layout="0aaoacmhcnacoaekhemaenheoaepagihgkaglogmhgnagohgpaiaaighiiaijoijhilaimoinbiohjaakaokaakehkgakhokhhkjakkokkokmhknakohkphlavlaamaomaamchmeamfomghmhamiomiomkhmlammomnbmohnavnavngvnivnkaoaooaCoahocaodooehofaogoogCogooiCoihojaokookCokoomhonaoohophpavpavpgvpivpkaqaoqaaqchqeaqfoqghqhaqioqioqkhqlaqmoqnbqohravraasaosaasehsgashoshhsjaskoskosmhsnasohsphtaauaaughuiaujoujhulaumounbuoawihwkawlowmhwnawohwpaykhymaynhyoaypaAmhAnaAoaCo")
#
r(5260, "Space Bridge", layout="0aaaaacaaeaagaaiaakaamaaoaaqhbbhbdhbfhbhhbjhblhbnhbpacaoccoceocgociockocmocoacqhdbvddvdfvdivdlvdnhdpaeaoecCeeCeiCemoeoaeqhfbvfdvfnhfpagaogcogoagqhhbhhpaiaoicoioaiqhjbajfajlhjpakaokchkghkkokoakqhlbvldClealholhaljoljClmvlnhlpamaomchmivmiomoamqhnbanhonhanjonjhnpaoaoochoghokoooaoqhpbapfaplhppaqaoqcoqoaqqhrbvrdvrnhrpasaoscCseCsiCsmosoasqhtbvtdvtfvtivtlvtnhtpauaoucoueougouioukoumouoauqhvbhvdhvfhvhhvjhvlhvnhvpawaawcaweawgawiawkawmawoawq")
r(5261, "Space Shuttle", layout="0aalaanacibckbcmaeebegbeibekbembgcbgecggcgicgkcgmbiacicciedigdiidikdimckadkcekeekgekiekkekmbmacmccmedmgdmidmkdmmbocboecogcoicokcomaqebqgbqibqkbqmasibskbsmaulaun")
r(5262, "Stage 1", layout="0aaebagaaiaccbceccgbciackaeabecceevefcegvehceibekaemagacgcdgedggdgicgkagmaiadicdiedigdiidikaimakadkcdkedkgdkidkkakmamacmcdmedmgdmicmkammaoaboccoevofcogvohcoibokaomaqcbqecqgbqiaqkasebsgasi")
r(5263, "Stage 2", layout="0aafaahaceacgaciaeeaegaeiagcbgebggbgiagkaiabicciecigciibikaimbkackcckeckgckickkbkmbmaombbmcomdbmepmfbmgpmhbmiomjbmkomlbmmboaoobbocoodboepofbogpohboioojbokoolbombqacqccqecqgcqicqkbqmasabsccsecsgcsibskasmaucbuebugbuiaukaweawgawiayeaygayiaAfaAh")
r(5264, "Stairs 2", layout="0aaadacaaedagaaidakacadccacedcgacidckbeadecbeedegbeidekbgacgcbgecggbgicgkciacicciecigciicikckabkcckebkgckibkkdmabmcdmebmgdmibmkdoaaocdoeaogdoiaokdqaaqcdqeaqgdqiaqk")
r(5265, "Stairs 3", layout="0eaeeageaieakeamdcfdchdcjdclcegceicekbgabghbgjbgqaicaiiaioalfaliallhmibnaanibnqaocioiaoobpaapibpqhqiarfariarlaucauiauobwabwhbwjbwqcygcyicykdAfdAhdAjdAleCeeCgeCieCkeCm")
r(5266, "Stargate", layout="0hagobeabgobgobihcehcghcjoddadeodgadiodkhechelafcofcafgpfgafkofmhgbhgghgnahaohaphgahmohohiahilhipajaojavjcvjevjgvjivjkajoojphkavkaokdokfokhokjhkpalaolaClavlchlehlghlivlkolpalqhmavmaomdamfamhomjhmpanaonaCnavnchnehnivnkanopnphoavoaoodaofaohoojhopapaopaCpavpchpehpghpivpkoppapqhqavqaoqdoqfoqhoqjhqparaoravrcvrevrgvrivrkaroorphsahslhspataotaptgatmotohubhughunavcovcavgpvgavkovmhwchwloxdaxeoxgaxioxkhyehyghyjozeazgozgozihAg")
#
r(5267, "Sukis", layout="0aaaaacaaeaagaaiaakaamaaoaaqhbbhbfhbjhbnacaaccaceacgaciackacmacoacqafaafcafeafgafiafkafmafoafqhgbhgpahaahcaheahgahiahkahmahoahqakahkbakcakeakgakiakkakmakoakqhlpamaamcameamgamiamkammamoamqapaapcapeapgapiapkapmapoapqhqbhqparaarcareargariarkarmaroarqauaaucaueaugauiaukaumauoauqhvpawahwbawcaweawgawiawkawmawoawqazaazcazeazgaziazkazmazoazqhAbhApaBaaBcaBeaBgaBiaBkaBmaBoaBqaEaaEcaEeaEgaEiaEkaEmaEoaEqhFbhFfhFjhFnaGaaGcaGeaGgaGiaGkaGmaGoaGq")
#
r(5268, "Temple 1", layout="0aaaaaeaaiabchbdabghbhacahcboccacehcfocgaciadchddodeadghdhaeaheboecaeehefoegaeiafchfdpfeafghfhagahgbogcagehgfoggagiahchhdvhdohevhfahghhhaiahiboicaiehifoigaiiajchjdvjdojeCjevjfajghjhakahkbokcakehkfokgakialchldvldoleClevlfalghlhamahmbomcamehmfomgamianchndvndoneCnevnfanghnhaoahoboocaoehofoogaoiapchpdvpdopevpfapghphaqahqboqcaqehqfoqgaqiarchrdprearghrhasahsboscasehsfosgasiatchtdoteatghthauahuboucauehufougauiavchvdavghvhawaaweawi")
#
r(5269, "Temple 2", layout="0aacaagaakabahbbabehbfabihbjaccocchcdacgocghchackadahdbadeodehdfadiodihdjaecoechedaegoeghehaekafahfbafeofehffafiofihfjagcogchgdaggpgghghagkahahhbahephehhfahiohihhjaicoichidaigpighihaikajahjbajepjehjfajiojihjjakcokchkdakgpkghkhakkalahlbaleplehlfaliolihljamcomchmdamgpmghmhamkanahnbaneonehnfanionihnjaocoochodaogooghohaokapahpbapeopehpfapiopihpjaqcoqchqdaqgoqghqhaqkarahrbareorehrfariorihrjaschsdasghshaskataateati")
r(5270, "Totally Random-Made", layout="0aaevajaaoabbhbhobioceCceacgaclCclpcmhddvddwdhhdmoecaedCedoeghejoenhffafgCfhafjofjCfkvfmagaCgfvggvgjhgkCgnahfohhChjahlohlahoaibhichieaihvihhiiojcajdojeCjiojjwjlojookmhkovkoClcClfvlgolhvliCljplkhlmvlmalpClpvmdhmghmjammCmmCncondCnganhCniankhodvodaoeCoehofhohvohvokoolvomaooCphopibplCpnvqharahreorfCrharkhrlormasfashvsiCsjhtfCthotiatjptnhtoaucoufhuhvuhauohvbavgovjCvjavkvvkhwghwjawnawpbxdaxjoxkayfaymayoaCdaCiaEiaFe")
r(5271, "Trika", layout="0hagaahiaiaajhakabfablhceicihcmaddoddodfadhvdhCdiadjvdjodladnodnheeieihemaffaflhggaghigiagjhgkciiakgokghkhakiokihkjakkokkhlfhllameomeamiammommhndhnnaocoocaogaoiaokaooooohpbhphhpjhppaqapqaaqehqfaqioqihqlaqmaqqpqqhrbhrhhrjhrpascoscasgasiaskasoosohtdhtnaueoueauiaumoumhvfhvlawgowghwhawiowihwjawkowkcyihAgaAhiAiaAjhAkaBfaBlhCeiCihCmaDdoDdoDfaDhvDhCDiaDjvDjoDlaDnoDnhEeiEihEmaFfaFlhGgaGhiGiaGjhGk")
r(5272, "Twin", layout="0aaeaagaaibccbcebcgbcibckaeabecceecegceibekaemagabgccgedggcgibgkagmaiabicciecigciibikaimbkcbkebkgbkibkkbmebmgbmibocboebogboibokaqabqccqecqgcqibqkaqmasabsccsedsgcsibskasmauabuccuecugcuibukaumbwcbwebwgbwibwkayeaygayi")
#
r(5273, "Two Domes", layout="0aaiabghbiabkacehcghckacmhdeodhodjhdmaecoefveioelaeohfdvfgvfkhfnagbogeCghCgjogmagphhcvhfvhlhhoaiaoidCigCikoinaiqhjcvjfajhvjlhjoakbokeCkhCkjokmakphldvlgvlkhlnamcomfvmiomlamohneonhonjhnmaoehoghokaomapghpiapkaqehqgoqhaqivqioqjhqkaqmarghriarkasehsghskasmhteothotjhtmaucoufvuioulauohvdvvgvvkhvnawboweCwhCwjowmawphxcvxfvxlhxoayaoydCygCykoynayqhzcvzfazhvzlhzoaAboAeCAhCAjoAmaAphBdvBgvBkhBnaCcoCfvCioClaCohDeoDhoDjhDmaEehEghEkaEmaFghFiaFkaGi")
#
r(5274, "Vagues", layout="0aacCaeaagCaiaakCamhbcvbehbgvbihbkvbmoccoceocgociockocmvdchdevdghdivdkhdmCecaeeCegaeiCekaemvfchfevfghfivfkhfmagaogcogeoggogiogkogmagohhahhcvhehhgvhihhkvhmhhooiaaicCieaigCiiaikCimoiovjahjcvjehjgvjihjkvjmvjoCkaokcokeokgokiokkokmCkovlavlchlevlghlivlkhlmvloomaCmcameCmgamiCmkammomohnavnchnevnghnivnkhnmhnoaoaoocooeoogooiookoomaoohpcvpehpgvpihpkvpmaqcCqeaqgCqiaqkCqmhrcvrehrgvrihrkvrmoscoseosgosioskosmvtchtevtghtivtkhtmCucaueCugauiCukaum")
r(5275, "Well2", layout="0aaaaacaaeaagaaiaakaamaaoacaccccceccgccicckccmacoaeadecdeedegdeidekdemaeoagadgcdgedgkdgmagoaiadicdiedikdimaioakadkcdkedkgdkidkkdkmakoamacmccmecmgcmicmkcmmamoaoaaocaoeaogaoiaokaomaoo")
#
r(5276, "Whatever", layout="0oaeoaghbdhbfhbhhcbaceoceacgocghcjadcadiheboeeoeghejafcafihgbogeogghgjahcwhfahioiahiboicoieoigoiihijoikajcvjdwjfvjhajiokahkbokcCkdokeokgCkhokihkjokkalcvldwlfvlhaliomahmbvmbomcCmdomeomgCmhomihmjvmjomkancvndwnfvnhaniooahobvoboocCodooeoogCohooihojvojookapcvpdwpfvphapioqahqboqcCqdoqeoqgCqhoqihqjoqkarcvrdwrfvrhariosahsboscoseosgosihsjoskatcwtfatihuboueoughujavcavihwboweowghwjaxcaxihybayeoyeaygoyghyjhzdhzfhzhoAeoAg")
r(5277, "Win", layout="0aaeaahaakaanbedbegbejbembepbhebhhbhkbhnbhqbjdbjgbjjbjmbjpbmcbmebmgbmibmkbmmbmococcoicoocqbcqhcqncsbcshcsncuacuccuecugcuicukcumcwbcwhcwncybcyhcyncAccAicAocCccCecCgcCicCkcCmcCo")
r(5278, "X-Files", layout="0aaaaaiaaqhbiacbacgaciociackacphdibecaeiaeoegdegneieeiidimdkfcklekpelbbmgbmkaocbohooibojaooaqahqbaqcoqchqdaqeaqiaqmhqnaqooqohqpaqqascbshosibsjasobugbukewbcwfcwlewpdyeeyidymeAdeAnaCcaCiaCohDiaEbaEgaEioEiaEkaEphFiaGaaGiaGq")
r(5279, "X-Shape", layout="0aaibbabbqcdabdcbdocdqaeicfacfcbfebfmcfocfqchabhcchebhgbhkchmbhochqbjabjecjgbjicjkbjmbjqblgdliblkbnabnecngbnicnkbnmbnqcpabpccpebpgbpkcpmbpocpqcracrcbrebrmcrocrqasictabtcbtoctqbvabvqawi")

