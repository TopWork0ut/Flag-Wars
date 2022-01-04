import pygame , sys
import random
import time
#h

def znov_z_pochatku():
    wikno = pygame.display.set_mode((1550,800),pygame.RESIZABLE)
    pygame.display.set_caption("Flag Wars")


    """частини екрану"""
    screenplay = pygame.Surface((1550,800))


    """частота кадрів"""
    clock = pygame.time.Clock()


    def load_image(name):
        fullname = "images"+"/"+name
        try:
            image = pygame.image.load(fullname).convert_alpha()
        except:
            print("can not  load image", name)
            raise SystemExit()
        return image

    def exit():
        pygame.quit()
        sys.exit()




    all_sprites =pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    block_sprites2 = pygame.sprite.Group()
    block_sprites3 = pygame.sprite.Group()
    block_sprites4 = pygame.sprite.Group()
    block_sprites5 = pygame.sprite.Group()
    block_sprites6 = pygame.sprite.Group()
    block_sprites7 = pygame.sprite.Group()
    block_sprites8 = pygame.sprite.Group()
    flags_verx_sprite = pygame.sprite.Group()
    prapor2 = pygame.sprite.Group()
    block_class_verx_drabini_group = pygame.sprite.Group()
    hero_stay_group = pygame.sprite.Group()
    strela_group = pygame.sprite.Group()
    GROUP_OF_SPRITE = pygame.sprite.Group()
    prapor = pygame.sprite.Group()
    bomb = pygame.sprite.Group()
    vibux = pygame.sprite.Group()

    hero_stay_group2 = pygame.sprite.Group()
    all_sprites2 = pygame.sprite.Group()
    pulia_group = pygame.sprite.Group()
    pulia2_group = pygame.sprite.Group()

    image_group = pygame.sprite.Group()

    pygame.font.init()

    """таймер кадрів"""
    #clock  = pygame.time.Clock()
    #dt = 0
    #complexity = None

    class image(pygame.sprite.Sprite):
        def __init__(self,x,y,image):
            super().__init__(image_group)
            self.image = load_image(image)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.add(image_group)


    complexity_2 = None
    class Settings:
          def __init__(self,punkts = [600,600, u"namePunkt",(250,250,30),(250,30,250)]):
             self.punkts = punkts
          def render(self,screenplay,font,num_punkt):
              for i in self.punkts:
                  if num_punkt == i[5]:
                      screenplay.blit(font.render(i[2],1,i[4]),(i[0],i[1]-30))
                  else:
                      screenplay.blit(font.render(i[2],1,i[3]),(i[0],i[1]-30))


          def settings(self):




              done2 = True
              font_menu = pygame.font.SysFont("courier new", 120 , bold = True)
              punkt = 0



              while done2:


                  #screenplay.fill((255, 213, 87))
                  #complexity = None


                  mouse = pygame.mouse.get_pos()
                  for i in self.punkts:
                      if mouse[0]>i[0] and mouse[0]<i[0]+600 and mouse[1]> i[1] and mouse[1]<i[1]+200:
                            punkt = i[5]
                      else:
                          pass
                  self.render(screenplay,font_menu,punkt)

                  for e in pygame.event.get():
                      if e.type == pygame.QUIT:
                          sys.exit()
                      if e.type == pygame.KEYDOWN:
                          if e.key == pygame.K_ESCAPE:
                              #sys.exit()
                              done = True
                          if e.key == pygame.K_UP:
                              if punkt > 0 :
                                  punkt -=1
                          if e.key == pygame.K_DOWN:
                              if punkt < len(self.punkts)-1:
                                  punkt+=1

                      if e.type ==pygame.MOUSEBUTTONDOWN  and e.button == 1:

                          if punkt == 0:
                               done2 = False
                               done = True
                          elif punkt == 1:
                              #sys.exit()
                              done2 = False
                              done = True

                          elif punkt == 2:
                            pass

                          elif punkt == 3:
                              complexity = 1
                              #punkts2 = [(640,280,u"Back",(50, 134, 237),(14, 86, 173),0),(440,390,u"Dont work :(",(24, 181, 2),(24, 181, 2),1),(500,500,u"Complexity :",(44, 237, 17),(24, 181, 2),2),(660,600,u"1",(250,30,250),(191, 2, 191),3),(730,600,u"2",(250,30,250),(191, 2, 191),4),(800,600,u"3",(250,30,250),(191, 2, 191),5)]
                          elif punkt == 4:
                              complexity = 2
                          elif punkt == 5:
                              complexity = 3

                  #image_1 = image(600,600,"keyboard-2170063_960_720player11.png")

                  wikno.blit(screenplay,(0,0))

                  screenplay.fill((255, 213, 87))

                  image_red = image(815,600,"keyboard_red.png")
                  image_1 = image(500,600,"keyboard-2170063_960_720player11.png")

                  image_group.draw(screenplay)
                  image_group.update()



                  pygame.display.flip()







    settings_true = True

    class Menu:
          def __init__(self,punkts = [600,600, u"namePunkt",(250,250,30),(250,30,250)]):
             self.punkts = punkts
          def render(self,screenplay,font,num_punkt):
              for i in self.punkts:
                  if num_punkt == i[5]:
                      screenplay.blit(font.render(i[2],1,i[4]),(i[0],i[1]-30))
                  else:
                      screenplay.blit(font.render(i[2],1,i[3]),(i[0],i[1]-30))


          def menu(self):


              done =True
              font_menu = pygame.font.SysFont("courier new", 120 , bold = True)
              punkt = 0
              while done:

                  screenplay.fill((255, 213, 87))



                  mouse = pygame.mouse.get_pos()
                  for i in self.punkts:
                      if mouse[0]>i[0] and mouse[0]<i[0]+600 and mouse[1]> i[1] and mouse[1]<i[1]+200:
                            punkt = i[5]
                      else:
                          pass
                  self.render(screenplay,font_menu,punkt)

                  for e in pygame.event.get():
                      if e.type == pygame.QUIT:
                          sys.exit()
                      if e.type == pygame.KEYDOWN:
                          if e.key == pygame.K_ESCAPE:
                              sys.exit()
                          if e.key == pygame.K_UP:
                              if punkt > 0 :
                                  punkt -=1
                          if e.key == pygame.K_DOWN:
                              if punkt < len(self.punkts)-1:
                                  punkt+=1

                      if e.type ==pygame.MOUSEBUTTONDOWN  and e.button == 1:
                          if punkt == 0:
                               done = False
                               settings_true = False
                          elif punkt == 1:
                              #done = False
                              settings_true = True


                              if settings_true == True:
                                  punkts2 = [(640,280,u"Back",(50, 134, 237),(14, 86, 173),0),(440,390,u"Dont work :(",(44, 237, 17),(24, 181, 2),1),(500,500,u"Keyboard:",(44, 237, 17),(24, 181, 2),2)]
                                  game2 = Settings(punkts2)
                                  game2.settings()


                                  if punkt == 3:
                                      complexity = 1
                                      #punkts2 = [(640,280,u"Back",(50, 134, 237),(14, 86, 173),0),(440,390,u"Dont work :(",(24, 181, 2),(24, 181, 2),1),(500,500,u"Complexity :",(44, 237, 17),(24, 181, 2),2),(660,600,u"1",(250,30,250),(191, 2, 191),3),(730,600,u"2",(250,30,250),(191, 2, 191),4),(800,600,u"3",(250,30,250),(191, 2, 191),5)]
                                  elif punkt == 4:
                                      complexity = 2
                                  elif punkt == 5:
                                      complexity = 3


                          elif punkt == 2:
                              sys.exit()
                              settings_true = False


                  image_block = image (500,600,"square.png")
                  image_version = image(30,700,"VERSION.png")

                  image_group.draw(screenplay)
                  image_group.update()

                  wikno.blit(screenplay,(0,0))
                  pygame.display.flip()


    """создання меню"""
    punkts = [(640,280,u"Play",(50, 134, 237),(14, 86, 173),0),(500,390,u"Settings",(44, 237, 17),(24, 181, 2),1),(640,500,u"Quit",(250,30,250),(191, 2, 191),2)]
    game = Menu(punkts)
    game.menu()

    class Menu2:
          def __init__(self,punkts = [600,600, u"namePunkt",(250,250,30),(250,30,250)]):
             self.punkts = punkts
          def render(self,screenplay,font,num_punkt):
              for i in self.punkts:
                  if num_punkt == i[5]:
                      screenplay.blit(font.render(i[2],1,i[4]),(i[0],i[1]-30))
                  else:
                      screenplay.blit(font.render(i[2],1,i[3]),(i[0],i[1]-30))


          def menu2(self):


              done =True
              font_menu = pygame.font.SysFont("courier new", 120 , bold = True)
              punkt = 0
              while done:

                  screenplay.fill((255, 213, 87))



                  mouse = pygame.mouse.get_pos()
                  for i in self.punkts:
                      if mouse[0]>i[0] and mouse[0]<i[0]+600 and mouse[1]> i[1] and mouse[1]<i[1]+200:
                            punkt = i[5]
                      else:
                          pass
                  self.render(screenplay,font_menu,punkt)

                  for e in pygame.event.get():
                      if e.type == pygame.QUIT:
                          sys.exit()
                      if e.type == pygame.KEYDOWN:
                          if e.key == pygame.K_ESCAPE:
                              sys.exit()
                          if e.key == pygame.K_UP:
                              if punkt > 0 :
                                  punkt -=1
                          if e.key == pygame.K_DOWN:
                              if punkt < len(self.punkts)-1:
                                  punkt+=1

                      if e.type ==pygame.MOUSEBUTTONDOWN  and e.button == 1:
                          if punkt == 0:
                               done = False
                               settings_true = False
                          elif punkt == 1:
                              #done = False
                              settings_true = True


                              if settings_true == True:
                                  punkts2 = [(640,280,u"Back",(50, 134, 237),(14, 86, 173),0),(440,390,u"Dont work :(",(44, 237, 17),(24, 181, 2),1),(500,500,u"Keyboard:",(44, 237, 17),(24, 181, 2),2)]
                                  game2 = Settings(punkts2)
                                  game2.settings()


                                  if punkt == 3:
                                      complexity = 1
                                      #punkts2 = [(640,280,u"Back",(50, 134, 237),(14, 86, 173),0),(440,390,u"Dont work :(",(24, 181, 2),(24, 181, 2),1),(500,500,u"Complexity :",(44, 237, 17),(24, 181, 2),2),(660,600,u"1",(250,30,250),(191, 2, 191),3),(730,600,u"2",(250,30,250),(191, 2, 191),4),(800,600,u"3",(250,30,250),(191, 2, 191),5)]
                                  elif punkt == 4:
                                      complexity = 2
                                  elif punkt == 5:
                                      complexity = 3


                          elif punkt == 2:
                              sys.exit()
                              settings_true = False

                          elif punkt == 3:
                               done = False

                  image_block = image (500,600,"square.png")
                  image_version = image(30,700,"VERSION.png")

                  image_group.draw(screenplay)
                  image_group.update()

                  wikno.blit(screenplay,(0,0))
                  pygame.display.flip()






    vbit_blue = []
    vbit_red = []



    class  flags_verx(pygame.sprite.Sprite):
        def __init__(self,x,y,image):
            super().__init__(flags_verx_sprite)
            self.image = load_image(image)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.add(flags_verx_sprite)



    class block_class(pygame.sprite.Sprite):
        def __init__(self,x,y,image):
            super().__init__(block_sprites)
            self.image = load_image(image)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.add(block_sprites)

    class block_class2(pygame.sprite.Sprite):
        def __init__(self,x,y,image):
            super().__init__(block_sprites2)
            self.image = load_image(image)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.add(block_sprites2)

    class block_class3(pygame.sprite.Sprite):
        def __init__(self,x,y,image):
            super().__init__(block_sprites3)
            self.image = load_image(image)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.add(block_sprites3)

    class block_class4(pygame.sprite.Sprite):
        def __init__(self,x,y,image):
            super().__init__(block_sprites4)
            self.image = load_image(image)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.add(block_sprites4)

    class block_class5(pygame.sprite.Sprite):
        def __init__(self,x,y,image):
            super().__init__(block_sprites5)
            self.image = load_image(image)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.add(block_sprites5)

    class block_class6(pygame.sprite.Sprite):
        def __init__(self,x,y,image):
            super().__init__(block_sprites6)
            self.image = load_image(image)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.add(block_sprites6)

    class block_class7(pygame.sprite.Sprite):
        def __init__(self,x,y,image):
            super().__init__(block_sprites7)
            self.image = load_image(image)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.add(block_sprites7)

    class block_class8(pygame.sprite.Sprite):
        def __init__(self,x,y,image):
            super().__init__(block_sprites8)
            self.image = load_image(image)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.add(block_sprites8)

    class block_class_verx_drabini(pygame.sprite.Sprite):
        def __init__(self,x,y,image):
            super().__init__(block_class_verx_drabini_group)
            self.image = load_image(image)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.add(block_class_verx_drabini_group)

    class AnimatedSprite_vibux(pygame.sprite.Sprite):
        def __init__(self, image, columns, rows, x, y,x_pos,y_pos ):
            super().__init__(vibux)
            #список фреймов для различных отрисовок спрайта
            self.frames = []
            self.cut_image(image, columns, rows)

            #изначально спрайт получает самый первый фрейм
            self.frame_number = 0
            self.image = self.frames[self.frame_number]
            self.rect = self.rect.move(x, y)

            self.rect.x =  x_pos
            self.rect.y =  y_pos
            self.speed_y = 0

            self.ONearth = False
            self.add(vibux)




        #функция для разрезания исходной картинки на фреймы
        #по заданному количество столбцов и строк
        #результат - список фреймов, начиная с самого первого фрейма
        def cut_image(self, image, columns, rows):
            self.rect = pygame.Rect(0, 0, image.get_width() // columns, image.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(image.subsurface(pygame.Rect(frame_location, self.rect.size)))

        #функция последовательной смены фреймов
        #если номер получаемого фрейма стал больше. нумерация повторяется с нуля
        def update(self):
            self.frame_number = (self.frame_number + 1) % len(self.frames)
            self.image = self.frames[self.frame_number]


    class AnimatedSprite_bomb(pygame.sprite.Sprite):
        def __init__(self, image, columns, rows, x, y,x_pos,y_pos ):
            super().__init__(bomb)
            #список фреймов для различных отрисовок спрайта
            self.frames = []
            self.cut_image(image, columns, rows)

            #изначально спрайт получает самый первый фрейм
            self.frame_number = 0
            self.image = self.frames[self.frame_number]
            self.rect = self.rect.move(x, y)

            self.rect.x =  x_pos
            self.rect.y =  y_pos
            self.speed_y = 0

            self.ONearth = False
            self.add(bomb)




        #функция для разрезания исходной картинки на фреймы
        #по заданному количество столбцов и строк
        #результат - список фреймов, начиная с самого первого фрейма
        def cut_image(self, image, columns, rows):
            self.rect = pygame.Rect(0, 0, image.get_width() // columns, image.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(image.subsurface(pygame.Rect(frame_location, self.rect.size)))

        #функция последовательной смены фреймов
        #если номер получаемого фрейма стал больше. нумерация повторяется с нуля
        def update(self):
            self.frame_number = (self.frame_number + 1) % len(self.frames)
            self.image = self.frames[self.frame_number]


            speed = 5

            if not pygame.sprite.groupcollide(bomb,block_sprites2,False,False):
                if not pygame.sprite.groupcollide(bomb,block_sprites5,False,False):
                    if not pygame.sprite.groupcollide(bomb,block_sprites4,False,False):
                        if not pygame.sprite.groupcollide(bomb,block_sprites7,False,False):
                            if not pygame.sprite.groupcollide(bomb,block_sprites8,False,False):
                                self.rect.y += speed




    class AnimatedSprite_prapor(pygame.sprite.Sprite):
        def __init__(self, image, columns, rows, x, y,x_pos,y_pos ):
            super().__init__(prapor)
            #список фреймов для различных отрисовок спрайта
            self.frames = []
            self.cut_image(image, columns, rows)

            #изначально спрайт получает самый первый фрейм
            self.frame_number = 0
            self.image = self.frames[self.frame_number]
            self.rect = self.rect.move(x, y)

            self.rect.x =  x_pos
            self.rect.y =  y_pos
            self.speed_y = 0

            self.vziat = False

            self.ONearth = False
            self.add(prapor)

            self.prapor_trimaetsa = False


        #функция для разрезания исходной картинки на фреймы
        #по заданному количество столбцов и строк
        #результат - список фреймов, начиная с самого первого фрейма
        def cut_image(self, image, columns, rows):
            self.rect = pygame.Rect(0, 0, image.get_width() // columns, image.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(image.subsurface(pygame.Rect(frame_location, self.rect.size)))

        #функция последовательной смены фреймов
        #если номер получаемого фрейма стал больше. нумерация повторяется с нуля
        def update(self):
            self.frame_number = (self.frame_number + 1) % len(self.frames)
            self.image = self.frames[self.frame_number]

            self.prapor_trimaetsa_hero = False
            self.prapor_trimaetsa_hero2 = False
            speed = 5
            if pygame.sprite.groupcollide(all_sprites,prapor,False,False) and self.vziat == False and not pygame.sprite.groupcollide(all_sprites,prapor2,False,False):


                    self.prapor_trimaetsa_hero =  True
                    self.rect.x = hero.rect.x + 43
                    self.rect.y = hero.rect.y - 30
                    speed = 0

            if pygame.sprite.groupcollide(all_sprites2,prapor,False,False) and self.vziat == False and not pygame.sprite.groupcollide(all_sprites2,prapor2,False,False):


                    self.prapor_trimaetsa_hero2 =  True
                    self.rect.x = hero2.rect.x + 43
                    self.rect.y = hero2.rect.y - 30
                    speed = 0

            elif  najatie.type == pygame.KEYDOWN  and najatie.key == pygame.K_m and ( pygame.sprite.groupcollide(prapor,all_sprites,False,False) or pygame.sprite.groupcollide(prapor,hero_stay_group,False,False)):
                    speed = 5
                    self.vziat = True


            elif  najatie.type == pygame.KEYDOWN  and najatie.key == pygame.K_q and ( pygame.sprite.groupcollide(prapor,all_sprites2,False,False) or pygame.sprite.groupcollide(prapor,hero_stay_group2,False,False)):
                    speed = 5
                    self.vziat = True



            if pygame.sprite.groupcollide(hero_stay_group,prapor,False,False) and self.vziat == False and not pygame.sprite.groupcollide(hero_stay_group,prapor2,False,False):


                    self.prapor_trimaetsa_hero =  True
                    self.rect.x = hero.rect.x + 43
                    self.rect.y = hero.rect.y - 30
                    speed = 0

            if pygame.sprite.groupcollide(hero_stay_group2,prapor,False,False) and self.vziat == False and not pygame.sprite.groupcollide(hero_stay_group2,prapor2,False,False):


                    self.prapor_trimaetsa_hero2 =  True
                    self.rect.x = hero2.rect.x + 43
                    self.rect.y = hero2.rect.y - 30
                    speed = 0



            elif  najatie.type == pygame.KEYDOWN  and najatie.key == pygame.K_m and ( pygame.sprite.groupcollide(prapor,all_sprites,False,False) or pygame.sprite.groupcollide(prapor,hero_stay_group,False,False)):
                    speed = 5
                    self.vziat = True


            elif  najatie.type == pygame.KEYDOWN  and najatie.key == pygame.K_q and ( pygame.sprite.groupcollide(prapor,all_sprites2,False,False) or pygame.sprite.groupcollide(prapor,hero_stay_group2,False,False)):
                    speed = 5
                    self.vziat = True


            else:
                self.prapor_trimaetsa_hero = False
                self.prapor_trimaetsa_hero2 = False
                if not pygame.sprite.groupcollide(prapor,block_sprites2,False,False):
                    if not pygame.sprite.groupcollide(prapor,block_sprites5,False,False):
                        if not pygame.sprite.groupcollide(prapor,block_sprites4,False,False):
                            if not pygame.sprite.groupcollide(prapor,block_sprites7,False,False):
                                if not pygame.sprite.groupcollide(prapor,block_sprites8,False,False):
                                    self.rect.y += speed
                                else:
                                    self.vziat = False
                            else:
                                self.vziat = False
                        else:
                            self.vziat = False
                    else:
                        self.vziat = False
                else:
                    self.vziat = False

            if pygame.sprite.groupcollide(block_sprites8,prapor,False,False) :
                flags_red.append(0)
                if flags_blue.count(0) > 0:
                    flags_blue.remove(0)
                self.rect.x = 0
                self.rect.y = 700



    class AnimatedSprite_prapor2(pygame.sprite.Sprite):
        def __init__(self, image, columns, rows, x, y,x_pos,y_pos ):
            super().__init__(prapor2)
            #список фреймов для различных отрисовок спрайта
            self.frames = []
            self.cut_image(image, columns, rows)

            #изначально спрайт получает самый первый фрейм
            self.frame_number = 0
            self.image = self.frames[self.frame_number]
            self.rect = self.rect.move(x, y)

            self.rect.x =  x_pos
            self.rect.y =  y_pos
            self.speed_y = 0

            self.vziat = False

            self.ONearth = False
            self.add(prapor2)

            self.prapor_trimaetsa = False


        #функция для разрезания исходной картинки на фреймы
        #по заданному количество столбцов и строк
        #результат - список фреймов, начиная с самого первого фрейма
        def cut_image(self, image, columns, rows):
            self.rect = pygame.Rect(0, 0, image.get_width() // columns, image.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(image.subsurface(pygame.Rect(frame_location, self.rect.size)))

        #функция последовательной смены фреймов
        #если номер получаемого фрейма стал больше. нумерация повторяется с нуля
        def update(self):
            self.frame_number = (self.frame_number + 1) % len(self.frames)
            self.image = self.frames[self.frame_number]

            self.prapor_trimaetsa_hero = False
            self.prapor_trimaetsa_hero2 = False
            speed = 5
            if pygame.sprite.groupcollide(all_sprites,prapor2,False,False) and self.vziat == False and not pygame.sprite.groupcollide(all_sprites,prapor,False,False):


                    self.prapor_trimaetsa_hero =  True
                    self.rect.x = hero.rect.x + 35
                    self.rect.y = hero.rect.y - 30
                    speed = 0

            if pygame.sprite.groupcollide(all_sprites2,prapor2,False,False) and self.vziat == False and not pygame.sprite.groupcollide(all_sprites2,prapor,False,False):


                    self.prapor_trimaetsa_hero2 =  True
                    self.rect.x = hero2.rect.x + 35
                    self.rect.y = hero2.rect.y - 30
                    speed = 0

            elif  najatie.type == pygame.KEYDOWN  and najatie.key == pygame.K_m and ( pygame.sprite.groupcollide(prapor2,all_sprites,False,False) or pygame.sprite.groupcollide(prapor2,hero_stay_group,False,False)):
                    speed = 5
                    self.vziat = True


            elif  najatie.type == pygame.KEYDOWN  and najatie.key == pygame.K_q and ( pygame.sprite.groupcollide(prapor2,all_sprites2,False,False) or pygame.sprite.groupcollide(prapor2,hero_stay_group2,False,False)):
                    speed = 5
                    self.vziat = True




            if pygame.sprite.groupcollide(hero_stay_group,prapor2,False,False) and self.vziat == False and not pygame.sprite.groupcollide(hero_stay_group,prapor,False,False) :


                    self.prapor_trimaetsa_hero =  True
                    self.rect.x = hero.rect.x + 35
                    self.rect.y = hero.rect.y - 30
                    speed = 0

            if pygame.sprite.groupcollide(hero_stay_group2,prapor2,False,False) and self.vziat == False and not pygame.sprite.groupcollide(hero_stay_group2,prapor,False,False) :


                    self.prapor_trimaetsa_hero2 =  True
                    self.rect.x = hero2.rect.x + 35
                    self.rect.y = hero2.rect.y - 30
                    speed = 0


            elif  najatie.type == pygame.KEYDOWN  and najatie.key == pygame.K_m and ( pygame.sprite.groupcollide(prapor2,all_sprites,False,False) or pygame.sprite.groupcollide(prapor2,hero_stay_group,False,False)):
                    speed = 5
                    self.vziat = True


            elif  najatie.type == pygame.KEYDOWN  and najatie.key == pygame.K_q and ( pygame.sprite.groupcollide(prapor2,all_sprites2,False,False) or pygame.sprite.groupcollide(prapor2,hero_stay_group2,False,False)):
                    speed = 5
                    self.vziat = True


            else:
                self.prapor_trimaetsa_hero = False
                self.prapor_trimaetsa_hero2 = False
                if not pygame.sprite.groupcollide(prapor2,block_sprites2,False,False):
                    if not pygame.sprite.groupcollide(prapor2,block_sprites5,False,False):
                        if not pygame.sprite.groupcollide(prapor2,block_sprites4,False,False):
                            if not pygame.sprite.groupcollide(prapor2,block_sprites7,False,False):
                                if not pygame.sprite.groupcollide(prapor2,block_sprites8,False,False):
                                    self.rect.y += speed
                                else:
                                    self.vziat = False
                            else:
                                self.vziat = False
                        else:
                            self.vziat = False
                    else:
                        self.vziat = False
                else:
                    self.vziat = False

            if pygame.sprite.groupcollide(block_sprites7,prapor2,False,False) :
                if flags_red.count(0) > 0:
                    flags_red.remove(0)
                flags_blue.append(0)
                self.rect.x = 1500
                self.rect.y = 700

    class hero_stay(pygame.sprite.Sprite):
        def __init__(self,x,y,image):
            super().__init__(hero_stay_group)
            self.image = load_image(image)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed_y = 0
            self.add(hero_stay_group)

            self.ONearth = False


            self.isGround = False
            self.onEARTH = False


            self.level2 = False
            self.level1 = False

        def update(self):
            self.rect.y += self.speed_y


            if  pygame.sprite.groupcollide(hero_stay_group,block_sprites2,False,False) or pygame.sprite.groupcollide(hero_stay_group,block_sprites4,False,False) :

                self.ONearth = True
                onEARTH = True
                self.speed_y = 0
                self.rect.y += self.speed_y

                self.level1 = True
                self.level2 = False

            elif  pygame.sprite.groupcollide(hero_stay_group,block_sprites4,False,False):
                self.ONearth = True
                onEARTH = True
                self.level2 = True
                self.speed_y = 0
                self.rect.y += self.speed_y


                self.level1 = True
                self.level2 = False

            elif   self.rect.y < 425 and  pygame.sprite.groupcollide(hero_stay_group,block_sprites5,False,False):
                if pygame.sprite.groupcollide(hero_stay_group,block_sprites5,False,False):
                        self.level2 = True
                        self.ONearth = True
                        onEARTH = True
                        self.speed_y = 0
                        self.rect.y += self.speed_y

                        self.level1 = False

            elif   self.rect.y < 125 and  pygame.sprite.groupcollide(hero_stay_group,block_sprites7,False,False):
                if pygame.sprite.groupcollide(hero_stay_group,block_sprites7,False,False):
                        self.level2 = True
                        self.ONearth = True
                        onEARTH = True
                        self.speed_y = 0
                        self.rect.y += self.speed_y

                        self.level1 = False

            elif   self.rect.y < 125 and  pygame.sprite.groupcollide(hero_stay_group,block_sprites8,False,False):
                if pygame.sprite.groupcollide(hero_stay_group,block_sprites8,False,False):
                        self.level2 = True
                        self.ONearth = True
                        onEARTH = True
                        self.speed_y = 0
                        self.rect.y += self.speed_y

                        self.level1 = False

            else:

                #if not pygame.sprite.groupcollide(all_sprites,block_sprites2,False,False):
                    self.speed_y = 8
                    self.ONearth = False
                    onEARTH = False
                    self.rect.y += self.speed_y

            if pygame.sprite.groupcollide(hero_stay_group,bomb,True,True) :
                all_sprites.update()
                all_sprites.empty()
                kasanie = None
                kasanie = True
                hero = hero_stay(0,100,"NN_STAY_RIGHT.png")
                jivoi = False

                vibux.empty()
                b = None
                v = None
                v = red_bomb.rect.x
                b = hero.rect.y + 35

                vibux_ = AnimatedSprite_vibux(load_image("вибух-removebg-preview.png"),11,1,100,100,v,b)


        def move_up(self):
                self.rect.y = self.rect.y - 30

        def move_down(self):
                if not (pygame.sprite.groupcollide(hero_stay_group,block_sprites4,False,False)):
                    self.rect.y = self.rect.y + 10

        def move_right(self):
                self.rect.x = self.rect.x

        def move_left(self):
                self.rect.x = self.rect.x





    class AnimatedSprite_strela(pygame.sprite.Sprite):
        def __init__(self, image, columns, rows, x, y,x_pos,y_pos ):
            super().__init__(strela_group)
            #список фреймов для различных отрисовок спрайта
            self.frames = []
            self.cut_image(image, columns, rows)

            #изначально спрайт получает самый первый фрейм
            self.frame_number = 0
            self.image = self.frames[self.frame_number]
            self.rect = self.rect.move(x, y)

            self.rect.x =  x_pos
            self.rect.y =  y_pos
            self.speed_y = 0

            self.ONearth = False
            self.add(strela_group)

            self.isGround = False
            self.onEARTH = False

            self.pidiom = False
            self.level2 = False
            self.level1 = False
        #функция для разрезания исходной картинки на фреймы
        #по заданному количество столбцов и строк
        #результат - список фреймов, начиная с самого первого фрейма
        def cut_image(self, image, columns, rows):
            self.rect = pygame.Rect(0, 0, image.get_width() // columns, image.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(image.subsurface(pygame.Rect(frame_location, self.rect.size)))

        #функция последовательной смены фреймов
        #если номер получаемого фрейма стал больше. нумерация повторяется с нуля
        def update(self):
            self.frame_number = (self.frame_number + 1) % len(self.frames)
            self.image = self.frames[self.frame_number]


        def move_up(self):
                self.rect.y = self.rect.y - 30

        def move_down(self):
                self.rect.y = self.rect.y + 0.5

        def move_right(self):
                self.rect.x = self.rect.x + 40

        def move_left(self):
                self.rect.x = self.rect.x - 40



    class pulia(pygame.sprite.Sprite):
        def __init__(self,x,y,radius,color,facing):
            super().__init__(pulia_group)
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.facing = facing
            self.vel = 20 * facing
            self.image = load_image("blue_pulia.png") #pygame.draw.circle(screenplay,self.color,(self.x,self.y),self.radius)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.add(pulia_group)

        def draw(self,screenplay):
            pass#pygame.draw.circle(screenplay,self.color,(self.x,self.y),self.radius)
        def update(self):
            pass#self.rect.x += 20 * facing

    class pulia2(pygame.sprite.Sprite):
        def __init__(self,x,y,radius,color,facing):
            super().__init__(pulia2_group)
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.facing = facing2
            self.vel = 30
            self.vel = 20 * facing2
            self.image = load_image("red_pulia.png") #pygame.draw.circle(screenplay,self.color,(self.x,self.y),self.radius)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.add(pulia2_group)
            #self.vel = 30
        def draw(self,screenplay):
            pass#pygame.draw.circle(screenplay,self.color,(self.x,self.y),self.radius)
        def update(self):
            pass#self.rect.x += 20 * facing2

    class AnimatedSprite(pygame.sprite.Sprite):
        def __init__(self, image, columns, rows, x, y,x_pos,y_pos,GROUP_OF_SPRITE ):
            super().__init__(all_sprites)
            #список фреймов для различных отрисовок спрайта
            self.frames = []
            self.cut_image(image, columns, rows)

            #изначально спрайт получает самый первый фрейм
            self.frame_number = 0
            self.image = self.frames[self.frame_number]
            self.rect = self.rect.move(x, y)

            self.rect.x =  x_pos
            self.rect.y =  y_pos
            self.speed_y = 0

            self.ONearth = False
            self.add(all_sprites)

            self.isGround = False
            self.onEARTH = False


            self.level2 = False
            self.level1 = False
        #функция для разрезания исходной картинки на фреймы
        #по заданному количество столбцов и строк
        #результат - список фреймов, начиная с самого первого фрейма
        def cut_image(self, image, columns, rows):
            self.rect = pygame.Rect(0, 0, image.get_width() // columns, image.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(image.subsurface(pygame.Rect(frame_location, self.rect.size)))

        #функция последовательной смены фреймов
        #если номер получаемого фрейма стал больше. нумерация повторяется с нуля
        def update(self):
            self.frame_number = (self.frame_number + 1) % len(self.frames)
            self.image = self.frames[self.frame_number]



            self.rect.y += self.speed_y


            if  pygame.sprite.groupcollide(all_sprites,block_sprites2,False,False) or pygame.sprite.groupcollide(all_sprites,block_sprites4,False,False) :

                self.ONearth = True
                onEARTH = True
                self.speed_y = 0
                self.rect.y += self.speed_y

                self.level1 = True
                self.level2 = False

            elif  pygame.sprite.groupcollide(all_sprites,block_sprites4,False,False):
                self.ONearth = True
                onEARTH = True
                self.level2 = True
                self.speed_y = 0
                self.rect.y += self.speed_y


                self.level1 = True
                self.level2 = False

            elif   self.rect.y < 425 and  pygame.sprite.groupcollide(all_sprites,block_sprites5,False,False):
                if pygame.sprite.groupcollide(all_sprites,block_sprites5,False,False):
                        self.level2 = True
                        self.ONearth = True
                        onEARTH = True
                        self.speed_y = 0
                        self.rect.y += self.speed_y

                        self.level1 = False

            elif   self.rect.y < 125 and  pygame.sprite.groupcollide(all_sprites,block_sprites7,False,False):
                if pygame.sprite.groupcollide(all_sprites,block_sprites7,False,False):
                        self.level2 = True
                        self.ONearth = True
                        onEARTH = True
                        self.speed_y = 0
                        self.rect.y += self.speed_y

                        self.level1 = False

            elif   self.rect.y < 125 and  pygame.sprite.groupcollide(all_sprites,block_sprites8,False,False):
                if pygame.sprite.groupcollide(all_sprites,block_sprites8,False,False):
                        self.level2 = True
                        self.ONearth = True
                        onEARTH = True
                        self.speed_y = 0
                        self.rect.y += self.speed_y

                        self.level1 = False

            else:

                #if not pygame.sprite.groupcollide(all_sprites,block_sprites2,False,False):
                    self.speed_y = 8
                    self.ONearth = False
                    onEARTH = False
                    self.rect.y += self.speed_y



        def move_up(self):
                self.rect.y = self.rect.y - 30



        def move_down(self):
                if not (pygame.sprite.groupcollide(all_sprites,block_sprites4,False,False)):
                    self.rect.y = self.rect.y + 1


        def move_right(self):
                i = 5
                if vbit_blue.count(0) > 0:
                    i = 5 - vbit_blue.count(0) / 5
                    if vbit_red.count(0) > 20:
                        i = 1
                else : i = 5
                self.rect.x = self.rect.x + i


        def move_left(self):
                i = 5
                if vbit_blue.count(0) > 0:
                    i = 5 - vbit_blue.count(0) / 5
                    if vbit_red.count(0) > 20:
                        i = 1
                else : i = 5
                self.rect.x = self.rect.x - i






    """другий гравець"""

    class hero_stay2(pygame.sprite.Sprite):
        def __init__(self,x,y,image):
            super().__init__(hero_stay_group2)
            self.image = load_image(image)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed_y = 0
            self.add(hero_stay_group2)

            self.ONearth = False


            self.isGround = False
            self.onEARTH = False


            self.level2 = False
            self.level1 = False


        def update(self):
            self.rect.y += self.speed_y


            if  pygame.sprite.groupcollide(hero_stay_group2,block_sprites2,False,False) or pygame.sprite.groupcollide(hero_stay_group2,block_sprites4,False,False) :

                self.ONearth = True
                onEARTH = True
                self.speed_y = 0
                self.rect.y += self.speed_y

                self.level1 = True
                self.level2 = False

            elif  pygame.sprite.groupcollide(hero_stay_group2,block_sprites4,False,False):
                self.ONearth = True
                onEARTH = True
                self.level2 = True
                self.speed_y = 0
                self.rect.y += self.speed_y


                self.level1 = True
                self.level2 = False

            elif   self.rect.y < 425 and  pygame.sprite.groupcollide(hero_stay_group2,block_sprites5,False,False):
                if pygame.sprite.groupcollide(hero_stay_group2,block_sprites5,False,False):
                        self.level2 = True
                        self.ONearth = True
                        onEARTH = True
                        self.speed_y = 0
                        self.rect.y += self.speed_y

                        self.level1 = False

            elif   self.rect.y < 125 and  pygame.sprite.groupcollide(hero_stay_group2,block_sprites7,False,False):
                if pygame.sprite.groupcollide(hero_stay_group2,block_sprites7,False,False):
                        self.level2 = True
                        self.ONearth = True
                        onEARTH = True
                        self.speed_y = 0
                        self.rect.y += self.speed_y

                        self.level1 = False

            elif   self.rect.y < 125 and  pygame.sprite.groupcollide(hero_stay_group2,block_sprites8,False,False):
                if pygame.sprite.groupcollide(hero_stay_group2,block_sprites8,False,False):
                        self.level2 = True
                        self.ONearth = True
                        onEARTH = True
                        self.speed_y = 0
                        self.rect.y += self.speed_y

                        self.level1 = False

            else:

                #if not pygame.sprite.groupcollide(all_sprites,block_sprites2,False,False):
                    self.speed_y = 8
                    self.ONearth = False
                    onEARTH = False
                    self.rect.y += self.speed_y

            if pygame.sprite.groupcollide(hero_stay_group2,bomb,True,True) :
                all_sprites.update()
                all_sprites.empty()
                kasanie = None
                kasanie = True
                hero = hero_stay(0,100,"NN_STAY_RIGHT.png")
                jivoi = False

                vibux.empty()
                b = None
                v = None
                v = red_bomb.rect.x
                b = hero.rect.y + 35

                vibux_ = AnimatedSprite_vibux(load_image("вибух-removebg-preview.png"),11,1,100,100,v,b)


        def move_up(self):
                self.rect.y = self.rect.y - 30

        def move_down(self):
                if not (pygame.sprite.groupcollide(hero_stay_group2,block_sprites4,False,False)):
                    self.rect.y = self.rect.y + 10

        def move_right(self):

                self.rect.x = self.rect.x

        def move_left(self):


                self.rect.x = self.rect.x




    class AnimatedSprite2(pygame.sprite.Sprite):
        def __init__(self, image, columns, rows, x, y,x_pos,y_pos,GROUP_OF_SPRITE ):
            super().__init__(all_sprites2)
            #список фреймов для различных отрисовок спрайта
            self.frames = []
            self.cut_image(image, columns, rows)

            #изначально спрайт получает самый первый фрейм
            self.frame_number = 0
            self.image = self.frames[self.frame_number]
            self.rect = self.rect.move(x, y)

            self.rect.x =  x_pos
            self.rect.y =  y_pos
            self.speed_y = 0

            self.ONearth = False
            self.add(all_sprites2)

            self.isGround = False
            self.onEARTH = False


            self.level2 = False
            self.level1 = False
        #функция для разрезания исходной картинки на фреймы
        #по заданному количество столбцов и строк
        #результат - список фреймов, начиная с самого первого фрейма
        def cut_image(self, image, columns, rows):
            self.rect = pygame.Rect(0, 0, image.get_width() // columns, image.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(image.subsurface(pygame.Rect(frame_location, self.rect.size)))

        #функция последовательной смены фреймов
        #если номер получаемого фрейма стал больше. нумерация повторяется с нуля
        def update(self):
            self.frame_number = (self.frame_number + 1) % len(self.frames)
            self.image = self.frames[self.frame_number]



            self.rect.y += self.speed_y


            if  pygame.sprite.groupcollide(all_sprites2,block_sprites2,False,False) or pygame.sprite.groupcollide(all_sprites2,block_sprites4,False,False) :

                self.ONearth = True
                onEARTH = True
                self.speed_y = 0
                self.rect.y += self.speed_y

                self.level1 = True
                self.level2 = False

            elif  pygame.sprite.groupcollide(all_sprites2,block_sprites4,False,False):
                self.ONearth = True
                onEARTH = True
                self.level2 = True
                self.speed_y = 0
                self.rect.y += self.speed_y


                self.level1 = True
                self.level2 = False

            elif   self.rect.y < 425 and  pygame.sprite.groupcollide(all_sprites2,block_sprites5,False,False):
                if pygame.sprite.groupcollide(all_sprites2,block_sprites5,False,False):
                        self.level2 = True
                        self.ONearth = True
                        onEARTH = True
                        self.speed_y = 0
                        self.rect.y += self.speed_y

                        self.level1 = False

            elif   self.rect.y < 125 and  pygame.sprite.groupcollide(all_sprites2,block_sprites7,False,False):
                if pygame.sprite.groupcollide(all_sprites2,block_sprites7,False,False):
                        self.level2 = True
                        self.ONearth = True
                        onEARTH = True
                        self.speed_y = 0
                        self.rect.y += self.speed_y

                        self.level1 = False

            elif   self.rect.y < 125 and  pygame.sprite.groupcollide(all_sprites2,block_sprites8,False,False):
                if pygame.sprite.groupcollide(all_sprites2,block_sprites8,False,False):
                        self.level2 = True
                        self.ONearth = True
                        onEARTH = True
                        self.speed_y = 0
                        self.rect.y += self.speed_y

                        self.level1 = False

            else:

                #if not pygame.sprite.groupcollide(all_sprites,block_sprites2,False,False):
                    self.speed_y = 8
                    self.ONearth = False
                    onEARTH = False
                    self.rect.y += self.speed_y




        def move_up(self):
                self.rect.y = self.rect.y - 30



        def move_down(self):
                if not (pygame.sprite.groupcollide(all_sprites2,block_sprites4,False,False)):
                    self.rect.y = self.rect.y + 1


        def move_right(self):
                #self.rect.x = self.rect.x + 5
                i = 5
                if vbit_red.count(0) > 0:
                    i = 5 - vbit_red.count(0) / 5
                    if vbit_red.count(0) > 20:
                        i = 1
                else : i = 5
                self.rect.x = self.rect.x + i


        def move_left(self):
                #self.rect.x = self.rect.x - 5
                i = 5
                if vbit_red.count(0) > 0:
                    i = 5 - vbit_red.count(0) / 5
                    if vbit_red.count(0) > 20:
                        i = 1
                else : i = 5
                self.rect.x = self.rect.x - i


    level = ["...............................",
             "...............................",
             "...............................",
             ".%...........................%.",
             ".@...........................@.",
             "$@...........................@!",
             ".@...........................@.",
             ".@...........................@.",
             ".@......%.............%......@.",
             ".@......@.............@......@.",
             ".@......@&&&&&&&&&&&&&@......@.",
             ".@......@.............@......@.",
             ".@......@.............@......@.",
             ".@......@.............@......@.",
             ".*......*.............*......*.",
             ")))####)))###########)))####)))"]




    x = 0
    y = 0
    for row in level:
        for col in row:
            if col == ".":
                ice = block_class(x,y,"block.jpg")

            #if col == "+":
            #    ice = block_class6(x,y,"block.jpg")

            if col == "#":
                box1 = block_class2(x,y,"box.png")

            if col == "*":
                box2 = block_class3(x,y,"block3.jpg")

            if col == "@":
                box3 = block_class3(x,y,"block4.jpg")

            if col == "%":
                box4 = block_class_verx_drabini(x,y,"block2.jpg")

            if col == ")":
                box5 = block_class4(x,y,"box.png")

            if col == "&":
                box6 = block_class5(x,y,"box.png")

            if col == "$":
                box6 = block_class7(x,y,"box_blue.png")

            if col == "!":
                box7 = block_class8(x,y,"box_red.png")

            x += 50
        y+= 50
        x = 0

    start_time = time.monotonic()


    n = []
    u = []

    #def bombi_padaiut():
    #    x = random.randint(1,1400)
    #    red_bomb = AnimatedSprite_bomb(load_image("red_bomb-removebg-preview.png"),6,1,54,54,x,50)



    flags_blue = [0,0,0]
    flags_red = [0,0,0]


    image_for_hero = "NN_STAY_LEFT.png"

    hero = hero_stay(100,200,"NNSTAYRIGHT.png")
    hero2 = hero_stay2(1365,200,"NNSTAYLEFT2.png")

    blue_prapor = AnimatedSprite_prapor(load_image("FLAG_BLUE_PNG__2_-removebg-preview.png"),8,1,50,50,0,700)
    red_prapor = AnimatedSprite_prapor2(load_image("red_prapor_animation-removebg-preview.png"),8,1,50,50,1500,700)

    #for i in range(1111111):
    #    if i
    streli_left = []
    streli_right = []

    vzglad =None
    speed_walk = 10
    hero_animated_right = False

    pochatok_igri = True

    strela_letit = False

    jump_count = 10

    motion = "Stop"
    motion2 = "Stop"

    motion_3 = None



    strela_isnue = False
    vibux_isnue = False
    #z = random.randint(1,1400)
    rux = "stay"

    bullets = []
    bullets2 = []

    lastMove = "right"
    lastMove2 = "left"

    jivoi = True
    jivoi2 = True

    while pochatok_igri:

            if pygame.sprite.groupcollide(pulia_group,hero_stay_group2,True,True):
                #hero_stay_group2.empty()
                hero2 = hero_stay2(1460,110,"NNSTAYLEFT2.png")
                hero2.update()
                lastMove2 = "left"
                vbit_red.append(0)
                if vbit_blue.count(0) > 0:
                    vbit_blue.remove(0)

            if pygame.sprite.groupcollide(pulia_group,all_sprites2,True,True):
                #all_sprites2.empty()
                hero2 = hero_stay2(1460,110,"NNSTAYLEFT2.png")
                hero2.update()
                vbit_red.append(0)
                if vbit_blue.count(0) > 0:
                    vbit_blue.remove(0)
                lastMove2 = "left"


            if pygame.sprite.groupcollide(pulia2_group,hero_stay_group,True,True):
                #hero_stay_group2.empty()
                hero = hero_stay(0,110,"NNSTAYRIGHT.png")
                hero.update()
                lastMove = "right"
                vbit_blue.append(0)

                if vbit_red.count(0) > 0:
                    vbit_red.remove(0)

            if pygame.sprite.groupcollide(pulia2_group,all_sprites,True,True):
                #all_sprites2.empty()
                hero = hero_stay(0,110,"NNSTAYRIGHT.png")
                hero.update()
                vbit_blue.append(0)
                if vbit_red.count(0) > 0:
                    vbit_red.remove(0)
                lastMove = "right"


            if pygame.sprite.groupcollide(pulia_group,pulia2_group,True,True):
                pass

            for bullet in bullets:
                if bullet.rect.x < 1560 and bullet.rect.x > -50:
                    bullet.rect.x += bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))

            for bullet2 in bullets2:
                if bullet2.rect.x < 1560 and bullet2.rect.x > -50:
                    bullet2.rect.x += bullet2.vel
                else:
                    bullets2.pop(bullets2.index(bullet2))
            kasanie = None
            """стрільба"""
            keys = pygame.key.get_pressed()
            #if keys[pygame.K_f]:
            #for najatie in pygame.event.get():

            #n.append(0)

            #if n.count(0)// 25:
            #    vibux.empty()


            #if n.count(0) // 300:
            #        vibux.empty()
            #        bomb.empty()

                    #red_bomb = AnimatedSprite_bomb(load_image("red_bomb-removebg-preview.png"),6,1,54,54,random.randint(1,1450),50)
            #        n.clear()

            if flags_blue.count(0) > 6:
                pochatok_igri = False
                punkts = [(420,280,u"Play again",(50, 134, 237),(14, 86, 173),0),(500,390,u"Settings",(44, 237, 17),(24, 181, 2),1),(640,500,u"Quit",(250,30,250),(191, 2, 191),2),(460,0,u"Blue win!!!",(44, 44, 230),(0, 0, 194),3)]
                game = Menu2(punkts)
                game.menu2()

            if flags_red.count(0) > 6:
                pochatok_igri = False
                punkts = [(420,280,u"Play again",(50, 134, 237),(14, 86, 173),0),(500,390,u"Settings",(44, 237, 17),(24, 181, 2),1),(640,500,u"Quit",(250,30,250),(191, 2, 191),2),(460,0,u"Red win!!!",(247, 64, 54),(209, 11, 0),3)]
                game = Menu2(punkts)
                game.menu2()


            """ПРАПОРИ"""
            flags_verx_sprite.empty()
            if flags_blue.count(0) == 6 :
                flag_blue1 = flags_verx(0,0,"blue_prapor.png")
                flag_blue2 = flags_verx(50,0,"blue_prapor.png")
                flag_blue3 = flags_verx(100,0,"blue_prapor.png")
                flag_blue4 = flags_verx(150,0,"blue_prapor.png")
                flag_blue5 = flags_verx(200,0,"blue_prapor.png")
                flag_blue6 = flags_verx(250,0,"blue_prapor.png")

            if flags_blue.count(0) == 5 :
                flag_blue1 = flags_verx(0,0,"blue_prapor.png")
                flag_blue2 = flags_verx(50,0,"blue_prapor.png")
                flag_blue3 = flags_verx(100,0,"blue_prapor.png")
                flag_blue4 = flags_verx(150,0,"blue_prapor.png")
                flag_blue5 = flags_verx(200,0,"blue_prapor.png")

            if flags_blue.count(0) == 4 :
                flag_blue1 = flags_verx(0,0,"blue_prapor.png")
                flag_blue2 = flags_verx(50,0,"blue_prapor.png")
                flag_blue3 = flags_verx(100,0,"blue_prapor.png")
                flag_blue4 = flags_verx(150,0,"blue_prapor.png")

            if flags_blue.count(0) == 3 :
                flag_blue1 = flags_verx(0,0,"blue_prapor.png")
                flag_blue2 = flags_verx(50,0,"blue_prapor.png")
                flag_blue3 = flags_verx(100,0,"blue_prapor.png")

            if flags_blue.count(0) == 2 :
                flag_blue1 = flags_verx(0,0,"blue_prapor.png")
                flag_blue2 = flags_verx(50,0,"blue_prapor.png")

            if flags_blue.count(0) == 1 :
                flag_blue1 = flags_verx(0,0,"blue_prapor.png")



            if flags_red.count(0) == 6 :
                flag_red1 = flags_verx(1500,0,"red_prapor.png")
                flag_red2 = flags_verx(1450,0,"red_prapor.png")
                flag_red3 = flags_verx(1400,0,"red_prapor.png")
                flag_red4 = flags_verx(1350,0,"red_prapor.png")
                flag_red5 = flags_verx(1300,0,"red_prapor.png")
                flag_red6 = flags_verx(1250,0,"red_prapor.png")

            if flags_red.count(0) == 5 :
                flag_red1 = flags_verx(1500,0,"red_prapor.png")
                flag_red2 = flags_verx(1450,0,"red_prapor.png")
                flag_red3 = flags_verx(1400,0,"red_prapor.png")
                flag_red4 = flags_verx(1350,0,"red_prapor.png")
                flag_red5 = flags_verx(1300,0,"red_prapor.png")

            if flags_red.count(0) == 4 :
                flag_red1 = flags_verx(1500,0,"red_prapor.png")
                flag_red2 = flags_verx(1450,0,"red_prapor.png")
                flag_red3 = flags_verx(1400,0,"red_prapor.png")
                flag_red4 = flags_verx(1350,0,"red_prapor.png")

            if flags_red.count(0) == 3 :
                flag_red1 = flags_verx(1500,0,"red_prapor.png")
                flag_red2 = flags_verx(1450,0,"red_prapor.png")
                flag_red3 = flags_verx(1400,0,"red_prapor.png")

            if flags_red.count(0) == 2 :
                flag_red1 = flags_verx(1500,0,"red_prapor.png")
                flag_red2 = flags_verx(1450,0,"red_prapor.png")

            if flags_red.count(0) == 1 :
                flag_red1 = flags_verx(1500,0,"red_prapor.png")





            if pygame.sprite.groupcollide(all_sprites,block_sprites7,False,False):
                u.append(0)
            if pygame.sprite.groupcollide(hero_stay_group,block_sprites7,False,False):
                u.append(0)

            if u.count(0) > 400:
                jivoi = True


            for najatie in pygame.event.get():
                """стрільба"""


                for bullet in bullets:
                    if pygame.sprite.groupcollide(pulia_group,hero_stay_group2,True,True):
                        bullets.pop(bullets.index(bullet))
                    elif pygame.sprite.groupcollide(pulia_group,all_sprites2,True,True):
                        bullets.pop(bullets.index(bullet))






                if najatie.type == pygame.KEYDOWN and najatie.key == pygame.K_BACKSPACE:
                    if lastMove == "right":
                        facing = 1
                    else :
                        facing = -1

                    if len(bullets) < 100:
                        bullets.append(pulia(round(hero.rect.x + 20 ),round(hero.rect.y + 103),4,(0,0,255),facing))


                if najatie.type == pygame.KEYDOWN and najatie.key == pygame.K_h:
                    if lastMove2 == "right":
                        facing2 = 1
                    else :
                        facing2 = -1

                    if len(bullets2) < 100:
                        bullets2.append(pulia2(round(hero2.rect.x + 20 ),round(hero2.rect.y + 103),4,(255,0,0),facing2))



                JUMP_HERO = None
                hero_perezariadka_jump = None
                pidiom = None
                if  pygame.sprite.groupcollide(all_sprites,block_class_verx_drabini_group,False,False) or pygame.sprite.groupcollide(all_sprites,block_sprites3,False,False):
                    if hero.level1 == False or hero.level2 == False:
                        pidiom = False
                else:
                    pidiom = True

                if  pygame.sprite.groupcollide(hero_stay_group,block_class_verx_drabini_group,False,False) or pygame.sprite.groupcollide(hero_stay_group,block_sprites3,False,False):
                    if hero.level1 == False or hero.level2 == False:
                        pidiom = False
                else:
                    pidiom = True

                """для другого гравця"""
                if  pygame.sprite.groupcollide(all_sprites2,block_class_verx_drabini_group,False,False) or pygame.sprite.groupcollide(all_sprites2,block_sprites3,False,False):
                    if hero.level1 == False or hero.level2 == False:
                        pidiom = False
                else:
                    pidiom = True

                if  pygame.sprite.groupcollide(hero_stay_group2,block_class_verx_drabini_group,False,False) or pygame.sprite.groupcollide(hero_stay_group2,block_sprites3,False,False):
                    if hero.level1 == False or hero.level2 == False:
                        pidiom = False
                else:
                    pidiom = True

                if najatie.type == pygame.QUIT :
                        pygame.quit()
                        sys.exit()



                if najatie.type == pygame.KEYDOWN and najatie.key == pygame.K_RIGHT :
                        #strela_group.empty()
                        rux = "go_right"

                        x_right = None
                        x_right = hero.rect.x
                        y_right = None
                        y_right = hero.rect.y
                        hero_stay_group.empty()
                        all_sprites.empty()
                        image_for_hero =  "NNn.png"

                        hero = AnimatedSprite(load_image(image_for_hero),13,1,84,142,x_right,y_right,all_sprites)
                        hero.update()

                        all_sprites.update()



                        if   hero.rect.x <= 1470 :
                            hero.move_right()
                        motion =  "RIGHT"
                        vzglad = "RIGHT"

                        if blue_prapor.prapor_trimaetsa_hero == True:
                            blue_prapor.rect.x = hero.rect.x + 47
                            blue_prapor.rect.y = hero.rect.y - 30

                        hero_perzariadka_isnue = False

                        vzglad_for_right = True
                        vzglad_for_left = True

                        lastMove = "right"
                """вправо для другого гравця"""
                if najatie.type == pygame.KEYDOWN and najatie.key == pygame.K_d: #and jivoi2 == True:
                        #strela_group.empty()
                        rux = "go_right2"

                        x_right = None
                        x_right = hero2.rect.x
                        y_right = None
                        y_right = hero2.rect.y
                        hero_stay_group2.empty()
                        all_sprites2.empty()
                        image_for_hero =  "NNn2.png"

                        hero2 = AnimatedSprite2(load_image(image_for_hero),13,1,84,142,x_right,y_right,all_sprites)
                        hero2.update()

                        all_sprites2.update()



                        if   hero2.rect.x <= 1470 :
                            hero2.move_right()
                        motion2 =  "RIGHT"
                        vzglad2 = "RIGHT"

                        if blue_prapor.prapor_trimaetsa_hero2 == True:
                            blue_prapor.rect.x = hero2.rect.x + 47
                            blue_prapor.rect.y = hero2.rect.y - 30

                        hero_perzariadka_isnue = False

                        vzglad_for_right2 = True
                        vzglad_for_left2 = True

                        lastMove2 = "right"

                if najatie.type == pygame.KEYDOWN and najatie.key == pygame.K_LEFT :
                        rux = "go_left"
                        #strela_group.empty()

                        x_left = None
                        x_left = hero.rect.x
                        y_left = None
                        y_left = hero.rect.y
                        all_sprites.empty()
                        hero_stay_group.empty()

                        image_for_hero = "NNnn.png"
                        hero = AnimatedSprite(load_image(image_for_hero),13,1,84,142,x_left,y_left,all_sprites)
                        hero.update()

                        all_sprites.update()
                        if  hero.rect.x >= - 10  :
                            hero.move_left()
                        motion = "LEFT"
                        vzglad == "LEFT"
                        hero_perzariadka_isnue = False

                        if blue_prapor.prapor_trimaetsa_hero == True:
                            blue_prapor.rect.x = hero.rect.x + 47
                            blue_prapor.rect.y = hero.rect.y - 30

                        vzglad_for_right = True
                        vzglad_for_left = True

                        lastMove = "left"

                """рух другого гравця вліво"""
                if najatie.type == pygame.KEYDOWN and najatie.key == pygame.K_a :
                        rux2 = "go_left"
                        #strela_group.empty()

                        x_left = None
                        x_left = hero2.rect.x
                        y_left = None
                        y_left = hero2.rect.y
                        all_sprites2.empty()
                        hero_stay_group2.empty()

                        image_for_hero = "NNnn2.png"
                        hero2 = AnimatedSprite2(load_image(image_for_hero),13,1,84,142,x_left,y_left,all_sprites)
                        hero2.update()

                        all_sprites2.update()
                        if  hero2.rect.x >= - 10  :
                            hero2.move_left()
                        motion2 = "LEFT"
                        vzglad2 = "LEFT"


                        if blue_prapor.prapor_trimaetsa_hero2  == True:
                            blue_prapor.rect.x = hero2.rect.x + 47
                            blue_prapor.rect.y = hero2.rect.y - 30


                        lastMove2 = "left"

                if najatie.type == pygame.KEYUP and najatie.key == pygame.K_RIGHT:
                        rux = "stay"

                        x = None
                        x = hero.rect.x
                        y = None
                        y = hero.rect.y
                        all_sprites.empty()

                        if pygame.sprite.groupcollide(hero_stay_group,block_sprites7,False,False):
                            x = 0
                            y = 100
                            jivoi = False

                        hero_stay_group.empty()



                        image_for_hero = "new_stayy.png"
                        hero = hero_stay(x,y,"NNSTAYRIGHT.png")
                        hero.update()

                        all_sprites.update()
                        motion = "STOP"
                        vzglad = "RIGHT"

                        hero_perzariadka_isnue = False

                        move_up = None
                        move_down = None
                        move_up = True
                        move_down = True

                        if blue_prapor.prapor_trimaetsa_hero == True:
                            blue_prapor.rect.x = hero.rect.x + 47
                            blue_prapor.rect.y = hero.rect.y - 30


                        vzglad_for_right = True
                        vzglad_for_left = True

                        lastMove = "right"
                """другий гравець стоїть вправо"""
                if najatie.type == pygame.KEYUP and najatie.key == pygame.K_d:
                        rux2 = "stay"

                        x = None
                        x = hero2.rect.x
                        y = None
                        y = hero2.rect.y
                        all_sprites2.empty()

                        if pygame.sprite.groupcollide(hero_stay_group2,block_sprites7,False,False):
                            x = 0
                            y = 100
                            jivoi2 = False

                        hero_stay_group2.empty()



                        image_for_hero = "new_stayy.png"
                        hero2 = hero_stay2(x,y,"NNSTAYRIGHT2.png")
                        hero2.update()


                        motion2 = "STOP"
                        vzglad2 = "RIGHT"


                        move_up2 = None
                        move_down2 = None
                        move_up2 = True
                        move_down2 = True

                        if blue_prapor.prapor_trimaetsa_hero2  == True:
                            blue_prapor.rect.x = hero2.rect.x + 47
                            blue_prapor.rect.y = hero2.rect.y - 30




                        lastMove2 = "right"

                if najatie.type == pygame.KEYUP and najatie.key == pygame.K_LEFT:
                        rux = "stay"

                        x = None
                        x = hero.rect.x
                        y = None
                        y = hero.rect.y
                        all_sprites.empty()

                        if pygame.sprite.groupcollide(hero_stay_group,block_sprites7,False,False):
                            x = 0
                            y = 100
                            jivoi = False

                        hero_stay_group.empty()

                        image_for_hero = "new_stay22.png"
                        hero = hero_stay(x,y,"NNSTAYLEFT.png")
                        hero.update()

                        all_sprites.update()
                        motion = "STOP"
                        vzglad = "LEFT"

                        hero_perzariadka_isnue = False

                        move_up = None
                        move_down = None
                        move_up = True
                        move_down = True

                        if blue_prapor.prapor_trimaetsa_hero == True:
                            blue_prapor.rect.x = hero.rect.x + 47
                            blue_prapor.rect.y = hero.rect.y - 30

                        vzglad_for_right = True
                        vzglad_for_left = True

                        lastMove = "left"
                """другий гравець стоїть вліво"""
                if najatie.type == pygame.KEYUP and najatie.key == pygame.K_a:
                        rux2 = "stay"

                        x = None
                        x = hero2.rect.x
                        y = None
                        y = hero2.rect.y
                        all_sprites2.empty()

                        if pygame.sprite.groupcollide(hero_stay_group2,block_sprites7,False,False):
                            x = 0
                            y = 100
                            jivoi2 = False

                        hero_stay_group2.empty()

                        image_for_hero = "new_stay22.png"
                        hero2 = hero_stay2(x,y,"NNSTAYLEFT2.png")
                        hero2.update()

                        all_sprites2.update()
                        motion2 = "STOP"
                        vzglad2 = "LEFT"



                        move_up2 = None
                        move_down2 = None
                        move_up2 = True
                        move_down2 = True

                        if blue_prapor.prapor_trimaetsa_hero2  == True:
                            blue_prapor.rect.x = hero2.rect.x + 47
                            blue_prapor.rect.y = hero2.rect.y - 30



                        lastMove2 = "left"


            if motion == "RIGHT"  and hero.rect.x <= 1470 :
                hero.move_right()


            if motion == "LEFT" and hero.rect.x >= - 10  :
                hero.move_left()



            if  motion2 ==  "RIGHT" and hero2.rect.x <= 1470 :
                hero2.move_right()

            if  motion2 == "LEFT" and hero2.rect.x >= - 10  :
                hero2.move_left()






            """ 1 гравець стрибок ----------------------------------------------------------------------------------------"""
            #keys = pygame.key.get_pressed()
            #if  keys[pygame.K_SPACE]:






            move_up = True
            move_down = True

            if najatie.type == pygame.KEYDOWN and najatie.key == pygame.K_UP and  move_up == True :
                if pygame.sprite.groupcollide(all_sprites,block_sprites3,False,False)  :
                    motion = "UP"

            if najatie.type == pygame.KEYDOWN and najatie.key == pygame.K_UP and  move_up == True :
                if pygame.sprite.groupcollide(hero_stay_group,block_sprites3,False,False)  :
                    motion = "UP"





            if najatie.type == pygame.KEYDOWN and najatie.key == pygame.K_DOWN and move_down == True :
                if pygame.sprite.groupcollide(all_sprites,block_sprites3,False,False)  :
                    #if not pygame.sprite.groupcollide(all_sprites,block_sprites4,False,False):
                        motion = "DOWN"


            if najatie.type == pygame.KEYDOWN and najatie.key == pygame.K_DOWN and move_down == True :
                if pygame.sprite.groupcollide(hero_stay_group,block_sprites3,False,False)  :
                    #if not pygame.sprite.groupcollide(all_sprites,block_sprites4,False,False):
                        motion = "DOWN"




            """для другого гравця"""
            if najatie.type == pygame.KEYDOWN and najatie.key == pygame.K_w and  move_up2 == True:
                if pygame.sprite.groupcollide(all_sprites2,block_sprites3,False,False)  :
                    motion2 = "UP"

            if najatie.type == pygame.KEYDOWN and najatie.key == pygame.K_w and  move_up2 == True :
                if pygame.sprite.groupcollide(hero_stay_group2,block_sprites3,False,False)  :
                    motion2 = "UP"





            if najatie.type == pygame.KEYDOWN and najatie.key == pygame.K_s and move_down2 == True :
                if pygame.sprite.groupcollide(all_sprites2,block_sprites3,False,False)  :
                    #if not pygame.sprite.groupcollide(all_sprites,block_sprites4,False,False):
                        motion2 = "DOWN"


            if najatie.type == pygame.KEYDOWN and najatie.key == pygame.K_s and move_down2 == True :
                if pygame.sprite.groupcollide(hero_stay_group2,block_sprites3,False,False)  :
                    #if not pygame.sprite.groupcollide(all_sprites,block_sprites4,False,False):
                        motion2 = "DOWN"

            #if pygame.sprite.groupcollide(all_sprites,bomb,True,True):
            #    pass

            #if pygame.sprite.groupcollide(hero_stay_group,bomb,True,True):
            #    pass

            #elif pygame.sprite.groupcollide(bomb,block_sprites2,True,False):
            #    bomb.empty()
            #elif   pygame.sprite.groupcollide(bomb,block_sprites5,True,False):
            #    bomb.empty()
            #elif  pygame.sprite.groupcollide(bomb,block_sprites4,True,False):
            #    bomb.empty()





            if motion == "UP" and pygame.sprite.groupcollide(all_sprites,block_sprites3,False,False) :
                hero.move_up()

            if motion == "UP" and pygame.sprite.groupcollide(hero_stay_group,block_sprites3,False,False) :
                hero.move_up()



            if motion == "DOWN" and pygame.sprite.groupcollide(all_sprites,block_sprites3,False,False) :
                hero.move_down()

            if motion == "DOWN" and pygame.sprite.groupcollide(hero_stay_group,block_sprites3,False,False) :
                hero.move_down()


            """для другого гравця"""
            if motion2 == "UP" and pygame.sprite.groupcollide(all_sprites2,block_sprites3,False,False) :
                hero2.move_up()

            if motion2 == "UP" and pygame.sprite.groupcollide(hero_stay_group2,block_sprites3,False,False) :
                hero2.move_up()



            if motion2 == "DOWN" and pygame.sprite.groupcollide(all_sprites2,block_sprites3,False,False) :
                hero2.move_down()

            if motion2 == "DOWN" and pygame.sprite.groupcollide(hero_stay_group2,block_sprites3,False,False) :
                hero2.move_down()



            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                exit()
            if keys[pygame.QUIT]:
                exit()





            clock.tick(70)

            wikno.blit(screenplay,(0,0))

            screenplay.fill((255,255,255))

            block_sprites.draw(screenplay)
            block_sprites.update()

            block_sprites2.draw(screenplay)
            block_sprites2.update()

            block_sprites3.draw(screenplay)
            block_sprites3.update()

            block_sprites4.draw(screenplay)
            block_sprites4.update()

            block_sprites5.draw(screenplay)
            block_sprites5.update()

            block_sprites6.draw(screenplay)
            block_sprites6.update()

            block_sprites7.draw(screenplay)
            block_sprites7.update()

            block_sprites8.draw(screenplay)
            block_sprites8.update()

            flags_verx_sprite.draw(screenplay)
            flags_verx_sprite.update()

            block_class_verx_drabini_group.draw(screenplay)
            block_class_verx_drabini_group.update()


            for bullet in bullets:
                bullet.draw(screenplay)

            for bullet2 in bullets2:
                bullet2.draw(screenplay)


            strela_group.draw(screenplay)
            strela_group.update()


            pulia_group.draw(screenplay)
            pulia_group.update()

            pulia2_group.draw(screenplay)
            pulia2_group.update()


            hero_stay_group.draw(screenplay)
            hero_stay_group.update()

            hero_stay_group2.draw(screenplay)
            hero_stay_group2.update()

            all_sprites.draw(screenplay)
            all_sprites.update()

            all_sprites2.draw(screenplay)
            all_sprites2.update()

            prapor.draw(screenplay)
            prapor.update()

            prapor2.draw(screenplay)
            prapor2.update()

            bomb.draw(screenplay)
            bomb.update()

            vibux.draw(screenplay)
            vibux.update()



            pygame.display.flip()

while 1:
  znov_z_pochatku()

