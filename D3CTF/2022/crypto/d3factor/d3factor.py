from Crypto.Util.number import bytes_to_long, getPrime
from secret import msg
from sympy import nextprime
from gmpy2 import invert
from hashlib import md5

flag = 'd3ctf{'+md5(msg).hexdigest()+'}'
p = getPrime(256)
q = getPrime(256)
assert p > q
n = p * q
e = 0x10001
m = bytes_to_long(msg)
c = pow(m, e, n)

N = pow(p, 7) * q
phi = pow(p, 6) * (p - 1) * (q - 1)
d1 = getPrime(2000)
d2 = nextprime(d1 + getPrime(1000))
e1 = invert(d1, phi)
e2 = invert(d2, phi)

print(f'c = {c}')
print(f'N = {N}')
print(f'e1 = {e1}')
print(f'e2 = {e2}')
'''
c = 2420624631315473673388732074340410215657378096737020976722603529598864338532404224879219059105950005655100728361198499550862405660043591919681568611707967
N = 1476751427633071977599571983301151063258376731102955975364111147037204614220376883752032253407881568290520059515340434632858734689439268479399482315506043425541162646523388437842149125178447800616137044219916586942207838674001004007237861470176454543718752182312318068466051713087927370670177514666860822341380494154077020472814706123209865769048722380888175401791873273850281384147394075054950169002165357490796510950852631287689747360436384163758289159710264469722036320819123313773301072777844457895388797742631541101152819089150281489897683508400098693808473542212963868834485233858128220055727804326451310080791
e1 = 425735006018518321920113858371691046233291394270779139216531379266829453665704656868245884309574741300746121946724344532456337490492263690989727904837374279175606623404025598533405400677329916633307585813849635071097268989906426771864410852556381279117588496262787146588414873723983855041415476840445850171457530977221981125006107741100779529209163446405585696682186452013669643507275620439492021019544922913941472624874102604249376990616323884331293660116156782891935217575308895791623826306100692059131945495084654854521834016181452508329430102813663713333608459898915361745215871305547069325129687311358338082029
e2 = 1004512650658647383814190582513307789549094672255033373245432814519573537648997991452158231923692387604945039180687417026069655569594454408690445879849410118502279459189421806132654131287284719070037134752526923855821229397612868419416851456578505341237256609343187666849045678291935806441844686439591365338539029504178066823886051731466788474438373839803448380498800384597878814991008672054436093542513518012957106825842251155935855375353004898840663429274565622024673235081082222394015174831078190299524112112571718817712276118850981261489528540025810396786605197437842655180663611669918785635193552649262904644919
'''