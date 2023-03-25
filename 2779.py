#PROBLEMA: 2779 - Álbum da Copa
albumsize=int(input())
figurinhas=int(input())
album=[]
for i in range(figurinhas):
        n=int(input())
        if(n not in album):
                album.append(n)
album_completado=len(album)
resposta=albumsize - album_completado
print(resposta)
