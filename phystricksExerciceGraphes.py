from phystricks import *
def ExerciceGraphes():

    liste_noms=["logarithme","lnvalabsolue","lnxplusun","valabsolueln","unplusln","sqrtln","lnsqrt"]
    pspicts,fig = MultiplePictures("ACUooQwcDMZ",len(liste_noms))


    for i,nom in enumerate(liste_noms):
        pspicts[i].mother.caption=liste_noms[i]

    r=1
    eps=exp(-2)
    # Fonctions
    x=var('x')
        
    f1=ln(x)
    f2=ln(abs(x))
    f3=ln(x+r)
    f4=ln(x)+r
    f5=abs(ln(x))
    f6=sqrt(ln(x))
    f7=ln(x**2)

        # Graphes
    F=[phyFunction(f1).graph(eps,2),(phyFunction(f2).graph(eps,2),phyFunction(f2).graph(-2, -eps)),phyFunction(f3).graph(eps-1,2),phyFunction(f4).graph(eps,2),phyFunction(f5).graph(eps,3),phyFunction(f6).graph(1,3),(phyFunction(f7).graph(eps,2),phyFunction(f7).graph(-2, -eps))]


        # Figures
    for i in range(0,len(pspicts)):
        pspicts[i].DrawGraphs(F[i])
        pspicts[i].DrawDefaultAxes()
        pspicts[i].dilatation(1)

        pspicts[0].BB.AddX(-0.5)
        pspicts[0].BB.AddY(3.5)

    pspicts[1].BB.AddX(-2)
    pspicts[1].BB.AddY(3)

    pspicts[2].BB.AddX(-2)
    pspicts[2].BB.AddY(3)

    pspicts[3].BB.AddX(-1)
    pspicts[3].BB.AddY(3)

    pspicts[4].BB.AddX(-2)
    pspicts[4].BB.AddY(3)
    pspicts[4].BB.AddY(-3)

    pspicts[5].BB.AddX(-2)
    pspicts[5].BB.AddY(3)
    pspicts[5].BB.AddY(-3)

    pspicts[6].BB.AddX(-2)
    pspicts[6].BB.AddY(3)

    
    fig.conclude()
    fig.write_the_file()
