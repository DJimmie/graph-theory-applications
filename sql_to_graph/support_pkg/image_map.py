
""" Pygame code for loading the image and accessing the cooresponding json file"""

import json
import pygame
# from prototype_1 import SystemGui.uid

def get_map_file(image_dict,image_path):

    map_file_path=f'{image_path}{image_dict}.json'
    # map_file_path=f'{image_dict}.json'
    try:
        with open(map_file_path, "r") as read_file:
            x = json.load(read_file)
        print(x)
        return x
    except FileNotFoundError:
        data=dict()
        with open(map_file_path, 'w') as outfile:
            json.dump(data, outfile)
            


def the_map(the_image,image_path):

    global map_dict
    map_dict=get_map_file(the_image,image_path)

    pygame.init()
    image_path=f'{image_path}{the_image}.png'
    # image_path=f'{the_image}.png'
    image=pygame.image.load(image_path)
    image_size=image.get_size()

    w=image_size[0]
    h=image_size[1]

    global screen
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption(the_image)

    screen.blit(image, (0, 0))
    rect=image.get_rect()
    # clock = pygame.time.Clock()

    done = False
    while not done:
        #Add this in loop.
        # clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        if pygame.mouse.get_pressed()[0]:
            # map_selection(pygame.mouse.get_pos())

            mouse_pos=pygame.mouse.get_pos()
            x=mouse_pos[0]
            y=mouse_pos[1]
            
            for k,v in map_dict.items():
                check=[v['pos'][0]<=x<=v['pos'][1],v['pos'][2]<=y<=v['pos'][3]]
                if all(check):
                    print(f"Map Item is: {k}\nThe UID: {map_dict[k]['uid']}")
                    done=True
                    
                    pygame.display.quit()
                    pygame.quit()
                    return (k,map_dict[k]['uid'])
                    # break
        if done:
            break
        else:       
            pygame.display.flip()