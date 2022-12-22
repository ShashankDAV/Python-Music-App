song_list=['Shambhu.mp3','NoLove.mp3','Passori.mp3','HeatWaves.mp3','Pepas.mp3','xyz.mp3']
wav_list=['a1.wav','a2.wav','a3.wav','a4.wav','a5.wav']

from tkinter import *
from pygame import mixer as m
from gtts import gTTS
from mutagen.mp3 import MP3
import time
import random

rt=Tk()

music='Yo'
a=0
i=0
j=1
idk=0
pl=True
pil=True
s=Scale(length=700,orient=HORIZONTAL,from_=0,to=3,showvalue=False,bg='cyan')
s.place(y=1050,x=10)

ctm='0:03'
m.init()
im=PhotoImage(file='a.png')
g0=1
lg='lightgrey'
f='Italic 9 bold'
l=[]
gel='TTS.mp3'

fr=Frame(bg=lg,height=1000,width=800)
fr.place(x=0,y=0)

def mi(e):
	global pl
	x=e.x
	y=e.y
	if pl:
		if (x>0 and x<800) and (y>100 and y<950):
			xe=random.choice(wav_list)
			rim=m.Sound(xe)
			m.Sound.play(rim)

def n_song():
	global i,j,tm,ctm,l
	lg=globals()
	lg['pl']=False
	lg['pil']=False
	p()
	play()
	m.music.stop()
	s.set(0)
	sl=song_list[i:j]
	i+=1
	j+=1
	rr=len(song_list)-2
	rrr=len(song_list)-1
	if l==[2,4,6,1,3,5]:
		rr=rr+2
		rrr=rrr+2
	else:
		rr=rr
		rrr=rrr
	if i>=rr:
		i=0
	if j>=rrr:
		j=1
	lg['gel']="".join(sl)
	audi=MP3(gel)
	aud=audi.info.length
	s.config(to=aud)
	lg['ctm']=time.strftime('%M:%S',time.gmtime(aud))
	g=s.get()
	tm=time.strftime('%M:%S',time.gmtime(g))
	lb.config(text=f'{tm} of {ctm}')
	l1.config(text=f'{gel}')

def play():
	global g0,src,gel
	kl=globals()
	if pl:
		m.music.load(gel)
		kl['music']='is_playing'
		m.music.set_volume(g0)
		m.music.play(loops=0)
		kl['pl']=False
		bu1.config(text='Stop')
		ct()
	else:
		lrg=globals()
		s.set(0)
		m.music.stop()
		kl['pl']=True
		bu1.config(text='Play')

def p():
	global music
	lrrg=globals()
	if music=='is_playing':
		if pl==False:
			if pil:
				m.music.pause()
				lrrg['idk']=1
				lrrg['pil']=False
				bu2.config(text='Unpause')
			else:
				m.music.unpause()
				lrrg['pil']=True
				lrrg['idk']=0
				bu2.config(text='Pause')
		else:
			pass
rbc=50
def up():
	global rbc
	glo=globals()
	frr=Frame(rt)
	frr.place(x=10,y=1220)
	sc=Scale(frr,from_=0,to=100,length=700,orient=HORIZONTAL,showvalue=False)
	sc.pack(side=BOTTOM)
	sc.set(rbc)
	scc=sc.get()
	sic=scc/100
	def x():
		frr.destroy()
	def st():
		scc=sc.get()
		sici=scc/100
		glo['rbc']=scc
		m.music.set_volume(sici)
		lab.config(text=f'Volume: {sici}')
		rt.after(100,st)
	def be1():
		l.append(1)
	def be2():
		l.append(2)
	def be3():
		l.append(3)
	def be4():
		l.append(4)
	def be5():
		l.append(5)
	def be6():
		l.append(6)
	def clr():
		l.clear()

	buuu=Button(frr,text='X',bg='red',command=x)
	buuu.pack(anchor='ne',side=TOP)
	buu1=Button(frr,text='1',command=be1)
	buu1.place(x=0,y=0)
	buu2=Button(frr,text='2',command=be2)
	buu2.place(x=90,y=0)
	buu3=Button(frr,text='3',command=be3)
	buu3.place(x=180,y=0)
	buu4=Button(frr,text='4',command=be4)
	buu4.place(x=270,y=0)
	buu5=Button(frr,text='5',command=be5)
	buu5.place(x=360,y=0)
	buu6=Button(frr,text='6',command=be6)
	buu6.place(x=450,y=0)
	ub=Button(frr,text='Clear',command=clr,width=1)
	ub.place(x=540,y=0)
	
	lab=Label(frr,text=f'Volume: {sic}',font=f)
	lab.pack(anchor='nw',side=TOP)
	st()

ra=0
def ct():
	global a,idk
	fg=globals()
	a-=1
	if idk==0:
		b=s.get()
		a+=1
		b+=1
		s.set(a)
		audi=MP3(gel)
		aud=audi.info.length
		lr=aud-1
		c=m.music.get_pos()/1000
		ic=int(c)
		fg['ra']=b
		if b==a:
			pass
		else:
			cb=int(b)
			m.music.set_pos(cb)
			s.set(b)
	else:
		a+=0
		s.set(ra)
	rt.after(1000,ct)
	
def clb():
	global ctm
	g=s.get()
	tm=time.strftime('%M:%S',time.gmtime(g))
	lb.config(text=f'{tm} of {ctm}')
	lb.after(1000,clb)

la1=Label(fr,image=im,fg='black',bg='lightgrey',font=f,height=1000)
la1.place(x=-100,y=60)

l1=Label(text=f'{gel}',height=2,font='Italic 12 bold',width=22,bg=lg)
l1.place(x=0,y=0)

b2=Button(fr,text='>>>',height=2,font=f,bg='grey',width=5,command=n_song)
b2.place(x=550,y=0)

bu2=Button(text='Pause',bg=lg,fg='black',command=lambda:[p()],font=f,height=2,width=10)
bu2.place(x=-30,y=1100)

bu1=Button(text='Play',bg=lg,fg='black',command=play,font=f,height=2,width=10)
bu1.place(x=230,y=1100)

bu3=Button(text='Volume',bg=lg,fg='black',command=up,font=f,height=2,width=10)
bu3.place(x=490,y=1100)

lb=Label(text=f'10:10',font=f,anchor=E)
lb.place(x=490,y=1000)
clb()

rt.bind('<Motion>',mi)
rt.mainloop()