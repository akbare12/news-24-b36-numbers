import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024
OUT=os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR','out'),'entry.png')
CREAM=(250,244,230); INK=(18,18,18); RED=(178,34,34); NAVY=(18,42,76); GOLD=(201,162,39); BLUE=(36,90,160); GREEN=(34,120,60); ORANGE=(200,90,20); SKY=(168,198,224); SEA=(176,205,228); LAND=(232,214,170)
def F(p,s):
    try: return ImageFont.truetype(p,s)
    except Exception: return ImageFont.load_default()
FS='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'; SS='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; SB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
fK=F(SB,9); fM=F(FS,27); fS=F(FS,10); fH=F(SB,11); fD=F(SS,8); fC=F(SB,8); fA=F(SS,8); fN=F(SB,16); fL=F(SS,7); fT=F(SB,7); fB=F(SB,10)
img=Image.new('RGB',(W,H),CREAM); d=ImageDraw.Draw(img)
def T(x,y,s,f,c=INK): d.text((x,y),s,font=f,fill=c)
def TR(x,y,s,f,c=INK): d.text((x-d.textlength(s,font=f),y),s,font=f,fill=c)
def wrap(t,f,w):
    ls=[]; cur=''
    for wd in t.split():
        z=(cur+' '+wd).strip()
        if d.textlength(z,font=f)<=w: cur=z
        else: ls.append(cur); cur=wd
    if cur: ls.append(cur)
    return ls
def chip(x,y,s,c):
    w=d.textlength(s,font=fT)+8; d.rounded_rectangle([x,y,x+w,y+11],2,fill=c); d.text((x+4,y+1),s,font=fT,fill=(255,255,255)); return w
CH={'CONFIRMED':GREEN,'OFFICIAL':BLUE,'REPORTED':(90,90,140),'CLAIM':ORANGE}
HERO=[("1","RIYADH · MIDDLE EAST","CONFIRMED","Houthi drone hits Riyadh's tallest tower again, 11 hurt","A Houthi drone struck the PIF tower, Riyadh's tallest, the second strike on it in a week. 11 hurt: 2 Saudi, 2 Indian, 3 Nepali, 4 Egyptian. (Saudi officials)","tower"),
("2","SHANGHAI · ASIA","OFFICIAL","China probes Shanghai party chief Chen Jining","Chen Jining, 62, is probed for \u201cserious violations\u201d, the 4th Politburo member to fall this year in the biggest elite shake-up yet. (CCDI)","gate"),
("3","NEW YORK · US / TECH","CONFIRMED","Huawei guilty on 10 of 12 counts","A US federal jury found Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud. Sentencing is set for Sep 2027. (US court)","court")]
CARDS=[("4","ZAPORIZHZHIA · EUROPE / WAR","REPORTED","Russian attacks kill 9 across Ukraine in a day","9 killed and 81 wounded as Russia launched 96 drones; 73 were shot down or jammed. (Ukrainian officials)","drone"),
("5","CAS · AFRICA / SPORT","OFFICIAL","CAS hands Senegal back the AFCON title","CAS restored the AFCON title to Senegal after Morocco forfeited 3-0, making it 1-0 to Senegal. (CAS)","trophy"),
("6","HORMUZ · MIDDLE EAST","REPORTED","IRGC attacks container ship in Hormuz","A container ship was attacked in Hormuz at 18:58 UTC and its navigation was disabled near Khasab, Oman. (UKMTO)","ship"),
("7","NEW YORK · WORLD / MARKETS","CONFIRMED","Dow closes above 50,000 for the first time","The Dow closed at 50,018, its first close above 50,000, while the Nasdaq fell 1.5% and the Taiex jumped 8.99% to a record. (Market close)","chart"),
("8","REDMOND · WORLD / TECH","REPORTED","Microsoft declares \u2018Code Red\u2019 after historic outage","After a 24-hour outage, the worst in Exchange Online history, Microsoft set a one-hour global recovery target with 5 workstreams. (Reuters)","server")]
CARDS+=[("9","ESKISEHIR · EUROPE","REPORTED","Turkish military helicopter crash kills 5","An AS-532 military helicopter crashed in Eskisehir, killing 5 people on board. (Turkish officials)","heli"),
("10","CARTAGENA · AMERICAS","REPORTED","Supermarket hostages: 25 held in Cartagena","25 people were held hostage in a Cartagena supermarket; 5 elderly women were freed and airport landings were halted for 45 minutes. (Colombian officials)","shop"),
("11","ADEN · MIDDLE EAST","REPORTED","Houthis advance within 60 km of Aden","Houthi forces advanced to within 60 km of Aden, Yemen, in their latest push south. (Wires)","arrow"),
("12","LAHJ · MIDDLE EAST","REPORTED","Saudi strikes kill 25, wound 6 in Yemen","Saudi strikes on a bus and truck in Wadi Maabaq, Lahj, killed or left missing 25 people and wounded 6. (Yemeni officials)","blast"),
("13","JIUQUAN · WORLD / SPACE","OFFICIAL","China names first foreign astronaut for Tiangong","The Shenzhou-24 crew was named as Tang Hongbo, Wu Yi and Muhammad Zeeshan Ali of Pakistan, the first foreigner on Tiangong. (CMSA)","rocket")]

ALSO=[("14","Ankara","Haftar visits Turkey for the first time."),("15","London","UK sanctions Houthis + 4 officials."),("16","Villavicencio","Car bomb injures 23."),("17","Gaza","Israel kills Hamas internal security chief."),("18","Baghdad","Iraq orders federal control of Kurdish oilfields."),("19","Gaza","Meningitis epidemic alert, 272 cases in Oct."),("20","DR Congo","Missing Cessna 208, rebels claim shootdown."),("21","Hanoi","Hot-pot explosion kills at least 6."),("22","Gulf of Finland","Ukraine hits Russian ship Sparta II."),("23","Kuala Lumpur","Malaysia to return thousands of migrants."),("24","Ulleungdo","S. Korea shelter order as Russian jets enter ADIZ."),("25","Dhaka","Hasina plans return on 16 Dec."),("26","The Hague","14 nations endorse ICJ Myanmar ruling."),("27","Jakarta","Indonesia nominates 2 VP candidates."),("28","Beijing","China sentences official Ma to death for spying."),("29","Brussels","NATO vows defence against space threat."),("30","Mexico City","El Chapo Isidro: US drone aided weekend capture."),("31","San Salvador","Bukele names 3 soldiers killed in Haiti."),("32","Ottawa","Pentagon rebukes Canada, only 41.9% of air fleet ready."),("33","Washington","US adds Megaspeed to trade blacklist."),("34","Kyiv","Zelensky urges Ukraine/Russia/US/Europe talks soon."),("35","Ras Al Khaimah","UAE bus-truck crash kills 13."),("36","London","England record 5,258 heat deaths, summer 2026."),("37","Kourou","Ariane 6 lofts 36 Amazon satellites."),("38","Cikande","Factory-fire toll rises to 26.")]
UTC=[("02:15","NATO vows space defence"),("08:16","Hanoi blast"),("10:42","Saudi strikes Yemen"),("14:27","Riyadh tower hit"),("16:51","Houthis 60 km from Aden"),("18:58","Hormuz ship attack"),("20:41","Huawei guilty")]
NUM=[("11","hurt in Riyadh"),("9","killed in Ukraine"),("50,018","Dow close"),("+8.99%","Taiex record"),("25","killed/missing in Yemen"),("26","Cikande fire toll"),("10/12","Huawei counts"),("96","drones at Ukraine")]
CONT=[[(-168,66),(-140,70),(-120,71),(-95,80),(-80,73),(-65,60),(-55,47),(-70,42),(-75,35),(-80,26),(-85,30),(-90,21),(-97,16),(-105,20),(-115,28),(-125,40),(-125,49),(-140,60),(-165,60)],[(-80,10),(-60,8),(-50,0),(-40,-10),(-35,-20),(-45,-30),(-60,-35),(-70,-50),(-70,-30),(-75,-15),(-80,0)],[(-17,15),(-10,30),(0,36),(10,37),(20,32),(30,31),(35,28),(43,12),(51,10),(48,0),(40,-15),(35,-25),(20,-35),(15,-30),(12,-5),(9,4),(-8,5)],[(-10,36),(-9,43),(0,46),(-2,50),(5,53),(10,57),(18,56),(21,55),(28,60),(30,70),(40,68),(60,69),(80,73),(100,76),(120,73),(140,72),(160,70),(178,66),(170,60),(160,55),(145,45),(140,40),(130,35),(127,33),(120,25),(110,20),(105,10),(100,8),(95,15),(90,22),(80,13),(75,8),(70,20),(60,25),(55,26),(50,30),(48,30),(44,29),(40,36),(35,36),(30,36),(25,40),(20,40),(15,44),(10,44),(5,43),(0,40),(-5,36),(-9,37)],[(-5,50),(-3,53),(-5,58),(-2,57),(0,53),(1,51)],[(130,31),(133,34),(137,35),(140,38),(141,42),(144,44),(141,40),(139,37)],[(113,-22),(114,-30),(120,-34),(130,-32),(140,-38),(150,-37),(153,-27),(146,-19),(142,-11),(136,-12),(130,-13),(122,-14),(114,-20)]]
PINS=[(24.7,46.7),(31.2,121.5),(40.7,-74.0),(47.8,35.2),(14.7,-17.4),(26.5,56.3),(40.7,-74.0),(47.7,-122.1),(39.8,30.5),(10.4,-75.5),(12.8,45.0),(13.0,44.9),(39.7,98.5)]
OFF={7:(16,-12),12:(18,10),9:(12,8)}
REG=[('Europe',9,BLUE),('Middle East',8,ORANGE),('Asia',8,GREEN),('Africa',2,GOLD),('Americas',7,RED),('World/Space',4,NAVY)]
def scene(x,y,w,h,k):
    d.rectangle([x,y,x+w,y+h],fill=(38,58,105) if k in('tower','drone','blast') else SKY,outline=INK); d.rectangle([x,y+h-12,x+w,y+h],fill=(96,116,84))
    if k=='tower': d.rectangle([x+w//2-11,y+6,x+w//2+11,y+h-12],fill=(18,18,42)); [d.rectangle([x+16+i*26,y+52+(i%2)*8,x+36+i*26,y+h-12],fill=(72,82,132)) for i in range(4)]; [d.rectangle([x+w-42-i*26,y+52+(i%2)*8,x+w-22-i*26,y+h-12],fill=(72,82,132)) for i in range(4)]; [d.rectangle([x+w//2-7+(i%2)*7,y+16+(i//2)*11,x+w//2-3+(i%2)*7,y+20+(i//2)*11],fill=(255,220,120)) for i in range(10)]; d.ellipse([x+w-44,y+10,x+w-24,y+30],fill=(120,120,120)); d.polygon([(x+22,y+18),(x+36,y+23),(x+22,y+28)],fill=(255,255,255))
    elif k=='gate': d.rectangle([x+14,y+26,x+w-14,y+h-12],fill=(150,40,40)); d.polygon([(x+8,y+28),(x+w//2,y+8),(x+w-8,y+28)],fill=GOLD); d.rectangle([x+w//2-12,y+40,x+w//2+12,y+h-12],fill=(60,20,20)); d.rectangle([x+w-52,y+h-34,x+w-16,y+h-16],fill=(255,255,255)); d.line([x+w-48,y+h-28,x+w-20,y+h-28],fill=INK); d.line([x+w-48,y+h-23,x+w-20,y+h-23],fill=INK)
    elif k=='court': d.polygon([(x+10,y+34),(x+w//2,y+10),(x+w-10,y+34)],fill=(220,210,180)); [d.rectangle([x+20+i*(w-50)//3,y+34,x+28+i*(w-50)//3,y+h-16],fill=(240,235,220)) for i in range(4)]; d.rectangle([x+8,y+h-16,x+w-8,y+h-12],fill=(180,170,150))
    elif k=='drone': d.rectangle([x+10,y+h//3,x+w-10,y+h-12],fill=(52,58,96)); [d.rectangle([x+16+i*24,y+h//3+2+(i%3)*3,x+30+i*24,y+h-12],fill=(96,102,150)) for i in range(5)]; d.ellipse([x+w//2-4,y+4,x+w//2+4,y+12],fill=(255,255,255)); d.line([x+w//2-16,y+8,x+w//2+16,y+8],fill=(255,255,255))
    elif k=='trophy': d.ellipse([x+w//2-14,y+2,x+w//2+14,y+14],fill=GOLD); d.rectangle([x+w//2-10,y+8,x+w//2+10,y+h-12],fill=GOLD); d.rectangle([x+w//2-3,y+h-14,x+w//2+3,y+h-12],fill=GOLD); d.polygon([(x+12,y+4),(x+24,y+9),(x+12,y+14)],fill=(0,120,60)); d.polygon([(x+w-24,y+4),(x+w-12,y+9),(x+w-24,y+14)],fill=(200,40,40))
    elif k=='ship': d.polygon([(x+10,y+h-16),(x+w-10,y+h-16),(x+w-24,y+h-4),(x+24,y+h-4)],fill=(30,60,110)); [d.rectangle([x+24+i*26,y+h-28,x+46+i*26,y+h-16],fill=(200,60,40) if i%2 else (40,140,90)) for i in range(4)]; d.rectangle([x+w-52,y+2,x+w-20,y+h-16],fill=(240,240,240))
    elif k=='chart': d.line([x+12,y+h-20,x+12,y+4],fill=INK); d.line([x+12,y+h-20,x+w-12,y+h-20],fill=INK); [d.rectangle([x+20+i*22,y+h-20-(2+i*2),x+34+i*22,y+h-20],fill=NAVY) for i in range(4)]; d.line([x+16,y+h-8,x+w-16,y+6],fill=GREEN,width=3)
    elif k=='server': d.rectangle([x+16,y+4,x+w-16,y+h-4],fill=(40,44,52)); [d.rectangle([x+24,y+8+i*6,x+w-24,y+12+i*6],fill=(70,76,88)) for i in range(3)]; d.rectangle([x+24,y+8,x+w-24,y+12],fill=RED)
    elif k=='heli': d.ellipse([x+w//2-26,y+8,x+w//2+18,y+20],fill=(90,110,70)); d.line([x+w//2-34,y+8,x+w//2+34,y+8],fill=INK,width=2); d.line([x+w//2+18,y+14,x+w-12,y+10],fill=(90,110,70),width=4); d.rectangle([x+w//2-20,y+20,x+w//2-12,y+h-4],fill=(70,90,60)); d.ellipse([x+w//2+2,y+12,x+w//2+10,y+18],fill=SKY)
    elif k=='shop': d.rectangle([x+12,y+8,x+w-12,y+h-4],fill=(200,170,120)); d.rectangle([x+12,y+8,x+w-12,y+16],fill=RED); [d.rectangle([x+16+i*24,y+8,x+28+i*24,y+16],fill=(255,255,255)) for i in range(4)]; d.rectangle([x+w//2-12,y+18,x+w//2+12,y+h-4],fill=(90,60,30))
    elif k=='arrow': d.line([x+14,y+h-8,x+w-20,y+6],fill=RED,width=4); d.polygon([(x+w-34,y+4),(x+w-12,y+4),(x+w-14,y+18)],fill=RED); d.ellipse([x+12,y+h-14,x+24,y+h-4],fill=NAVY); d.text((x+w-72,y+h-12),'60 km',font=fB,fill=RED)
    elif k=='blast': d.polygon([(x+w//2,y+6),(x+w//2+10,y+18),(x+w-16,y+16),(x+w//2+12,y+h-8),(x+w-8,y+h-14),(x+w//2+4,y+h-6),(x+w//2-8,y+h-8),(x+w//2-14,y+h-14),(x+8,y+h-16),(x+w//2-12,y+18),(x+16,y+16),(x+w//2-10,y+18)],fill=(240,160,30)); d.ellipse([x+w//2-9,y+12,x+w//2+9,y+24],fill=(80,80,80))
    elif k=='rocket': d.polygon([(x+w//2,y+4),(x+w//2+10,y+16),(x+w//2+7,y+h-12),(x+w//2-7,y+h-12),(x+w//2-10,y+16)],fill=(240,240,240)); d.ellipse([x+w//2-4,y+10,x+w//2+4,y+16],fill=SKY); d.polygon([(x+w//2-7,y+h-12),(x+w//2,y+h-4),(x+w//2+7,y+h-12)],fill=(255,140,0)); [d.ellipse([x+10+i*30,y+4+(i%2)*8,x+16+i*30,y+10+(i%2)*8],fill=(255,255,255)) for i in range(4)]
    else: [d.rectangle([x+10+i*26,y+30+(i%2)*10,x+30+i*26,y+h-12],fill=(70,70,110)) for i in range(5)]
d.rectangle([0,0,W,18],fill=RED); T(10,3,'THE WORLD ON ONE PAGE',fK,(255,255,255)); TR(1014,3,'38 STORIES · 6 REGIONS · 13 FIELDS',fK,(255,255,255))
T(10,20,'Tuesday 24 November 2026',fM); TR(1014,30,'ALL FROM TUESDAY 24 NOVEMBER 2026',fK,RED)
T(10,50,'Houthi drone hits Riyadh tower · China probes Chen Jining · Huawei guilty on 10 of 12 counts',fS,RED)
bx=8
for r,nm,cc in REG: d.rectangle([bx,66,bx+167,82],fill=cc); T(bx+8,69,r+' '+str(nm),fK,(255,255,255)); bx+=167
T(8,88,'THE DAY IN UTC',fC,RED); ux=104
for t,ev in UTC: s=t+' '+ev; T(ux,88,s,fA); ux+=d.textlength(s,font=fA)+14
d.line([8,106,1016,106],fill=RED); T(8,110,'THE DAY IN NUMBERS',fC,RED)
for i,(v,lb) in enumerate(NUM):
    cx=150+i*108; T(cx-d.textlength(v,font=fN)/2,108,v,fN,NAVY); [T(cx-d.textlength(l,font=fL)/2,126+j*8,l,fL) for j,l in enumerate(wrap(lb,fL,100))]
for i,(n,k,c,h,dk,sk) in enumerate(HERO):
    x=8+i*336; w=330; scene(x,144,w,96,sk); T(x,244,n+' '+k,fC,RED); cw=d.textlength(c,font=fT)+8; chip(x+w-cw,244,c,CH[c]); hl=wrap(h,fH,w); [T(x,260+j*13,l,fH) for j,l in enumerate(hl[:2])]; dl=wrap(dk,fD,w); [T(x,288+j*10,l,fD) for j,l in enumerate(dl[:3])]

for i,(n,k,c,h,dk,sk) in enumerate(CARDS):
    x=8+(i%5)*202; y=324+(i//5)*113; w=196; d.rectangle([x,y,x+w,y+110],fill=(255,255,255),outline=(200,190,170)); scene(x+1,y+1,w-2,30,sk); T(x+5,y+34,n+' '+k,fC,RED); hl=wrap(h,fH,w-10); [T(x+5,y+46+j*11,l,fH) for j,l in enumerate(hl[:2])]; dl=wrap(dk,fD,w-10); [T(x+5,y+68+j*10,l,fD) for j,l in enumerate(dl[:3])]; chip(x+5,y+99,c,CH[c])
T(8,552,'THE WORLD · 13 PLACES PINNED',fK,RED); mx0,my0,mw,mh=8,568,652,164
d.rectangle([mx0,my0,mx0+mw,my0+mh],fill=SEA,outline=INK)
def PX(lo): return mx0+(lo+170)/350*mw
def PY(la): return my0+(83-la)/138*mh
for poly in CONT: d.polygon([(PX(lo),PY(la)) for lo,la in poly],fill=LAND,outline=(140,120,70))
for i,(la,lo) in enumerate(PINS,1):
    px,py=PX(lo),PY(la); ox,oy=OFF.get(i,(0,0)); qx,qy=px+ox,py+oy
    if (ox,oy)!=(0,0): d.line([px,py,qx,qy],fill=RED,width=2)
    d.ellipse([qx-7,qy-7,qx+7,qy+7],fill=RED,outline=(255,255,255)); T(qx-d.textlength(str(i),font=fT)/2,qy-5,str(i),fT,(255,255,255))
for j,(r,nm,cc) in enumerate(REG): d.rectangle([672,568+j*14,684,578+j*14],fill=cc); T(688,567+j*14,r+' '+str(nm),fA)
T(672,656,'PINNED: 1 Riyadh · 2 Shanghai · 3 New York · 4 Zaporizhzhia',fL); T(672,666,'5 Dakar · 6 Hormuz · 7 New York · 8 Redmond · 9 Eskisehir',fL); T(672,676,'10 Cartagena · 11 Aden · 12 Lahj · 13 Jiuquan',fL)
[T(672,692+j*9,l,fL) for j,l in enumerate(wrap('Pins 3 and 7 share New York and pins 11 and 12 share Aden, so both pairs are offset with leader lines.',fL,340))]
T(672,712,'Pin 8 Redmond sits on the US west coast, below Canada.',fL); T(672,722,'Pins 3 and 7 sit on the US east coast.',fL)
T(8,740,'ALSO ON TUESDAY 24 NOVEMBER — 25 MORE STORIES',fK,RED)
for j,(n,city,txt) in enumerate(ALSO):
    col=0 if j<9 else (1 if j<17 else 2); row=j-(0 if col==0 else (9 if col==1 else 17)); x=8+col*338; y=758+row*17; ls=wrap(n+'. '+city+': '+txt,fA,330); T(x,y,ls[0],fA)
    if len(ls)>1: T(x,y+8,ls[1],fA)
d.rectangle([8,914,1016,984],outline=RED,width=2); T(14,918,'DATE CHECK',fK,RED)
dc="Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC. LEFT OUT (not 24 Nov): Hormuz mine claims (23 Nov) · Nvidia brings back Huang (23 Nov) · EU sanctions package 22 (23 Nov) · COP31 ends with no deal (22 Nov) · corvette Merkury sinks (22 Nov) · El Chapo Isidro arrested (Fri 20 Nov) · Cikande factory fire starts (Sat 21 Nov) · Trump hush-money appeal ruling (23 Nov). NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC) · MPR session picks VP (11 Dec) · Huawei sentencing (Sep 2027) · Hasina returns to Bangladesh (16 Dec)."
[T(14,934+j*10,l,fD) for j,l in enumerate(wrap(dc,fD,990))]
T(8,988,'Sources: dailysummaryof.com/world/2026-11-24 · Astrova News · Horizon · WSOC/AP · Reuters.',fL)
T(8,998,'CONFIRMED = 2+ outlets · OFFICIAL = on record · REPORTED = one outlet · CLAIM = one side\u2019s claim.',fL)
T(8,1008,'Scenes are drawn illustrations, not photographs.',fL)
os.makedirs(os.path.dirname(OUT) or '.',exist_ok=True); img.save(OUT)
