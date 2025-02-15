# Activitat 14 

### Commit 1: Configuració  projecte

Connectar amb la nova aplicació un cop creada.
![alt text](/TIC_BCN_AR/login/captures/image.png)

Treballar amb postgresql.
![alt text](/TIC_BCN_AR/login/captures/image-1.png)

Afegir  templates a la configuració.
![alt text](/TIC_BCN_AR/login/captures/image-2.png)

### Commit 2: creació de l’aplicació

Captura de la comanda per crea la nova aplicacio

![alt text](/TIC_BCN_AR/login/captures/image-22.png)

En TIC_BCN_AR/urls.py posem la url 
![alt text](/TIC_BCN_AR/login/captures/image1.png)

En la aplicacio de nom "login" login/urls.py posem les urls
![alt text](/TIC_BCN_AR/login/captures/image-11.png)

### Commit 3: model usuari:

comandes:
![alt text](/TIC_BCN_AR/login/captures/image111.png)

![alt text](/TIC_BCN_AR/login/captures/image-111.png)

la taula a la Base de dades:
![alt text](/TIC_BCN_AR/login/captures/image-222.png)

### Commit 4: formulari de login:

![alt text](/TIC_BCN_AR/login/captures/image123.png)

### Documentar la funcionalitat de login sense sessió.
La vista inici(request) carrega la plantilla inici.html sense verificar si l'usuari ha iniciat sessió. La vista formulari(request) gestiona l'autenticació a través d'un formulari valida les dades introduïdes. Si l'email i la contrasenya estan a la base de dades, es redirigeix a la pàgina d'inici en cas contrari es mostra un missatge d'error indicant "credencials errònies". Aquest sistema no guarda la sessió de l'usuari, de manera que cada cop que torni a la pàgina d'inici haurà de tornar a introduir les seves credencials.

### Documentar funcionalitat login amb sessió.
La vista formulari(request), primer  comprova si ja té una sessió activa ('user_id' in request.session). Si és així, es redirigeix directament a la pàgina d'inici sense necessitat de tornar a introduir credencials. Si no hay una sesion es mostra el formulari de login.

Busca l'email i la contrasenya introduïts i es busca un usuari amb aquest email a la base de dades. Si existeix i la contrasenya coincideix, es guarda el seu ID a la sessió (request.session['user_id'] = user.id), permetent guardan la autenticacio. Si les credencials són incorrectes es mostra "Credencials errònies". Asi permet que l'usuari es mantingui connectat fins que es tanqui la sessió amb el logout.

### Documentar la funcionalitat de logout:
La funció logout(request) elimina tota la informació de la sessió amb request.session.flush(). Quan es borra  la sessió l'usuari és redirigit automàticament al formulari de login. La funció inici(request) comprova si l'usuari té una sessió activa amb 'user_id' a request.session. Si l'usuari no ha iniciat sessió, és redirigit al formulari de login pero si te una sessio estara a la pàgina d'inici (inici.html).
