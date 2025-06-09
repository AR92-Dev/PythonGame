
import os



SCREENSIZE = (1400, 800)

IMAGEPATHS = {
    'choice': {
        'load_game': os.path.join(os.getcwd(), 'resources/images/choice/load_game.png'),
        'map1': os.path.join(os.getcwd(), 'resources/images/choice/map1.png'),
        'map1_black': os.path.join(os.getcwd(), 'resources/images/choice/map1_black.png'),
        'map1_red': os.path.join(os.getcwd(), 'resources/images/choice/map1_red.png'),
        'map2': os.path.join(os.getcwd(), 'resources/images/choice/map2.png'),
        'map2_black': os.path.join(os.getcwd(), 'resources/images/choice/map2_black.png'),
        'map2_red': os.path.join(os.getcwd(), 'resources/images/choice/map2_red.png'),
        'map3': os.path.join(os.getcwd(), 'resources/images/choice/map3.png'),
        'map3_black': os.path.join(os.getcwd(), 'resources/images/choice/map3_black.png'),
        'map3_red': os.path.join(os.getcwd(), 'resources/images/choice/map3_red.png'),
        'easy_1': os.path.join(os.getcwd(), 'resources/images/choice/Easy_1.png'),
        'easy_2': os.path.join(os.getcwd(), 'resources/images/choice/Easy_2.png'),
        'mid_1': os.path.join(os.getcwd(), 'resources/images/choice/Mid_1.png'),
        'mid_2': os.path.join(os.getcwd(), 'resources/images/choice/Mid_2.png'),
        'hard_1': os.path.join(os.getcwd(), 'resources/images/choice/Hard_1.png'),
        'hard_2': os.path.join(os.getcwd(), 'resources/images/choice/Hard_2.png'),
        'Easy_B': os.path.join(os.getcwd(), 'resources/images/choice/Easy_B.jpg'),
        'Mid_B': os.path.join(os.getcwd(), 'resources/images/choice/Mid_B.jpg'),
        'Hard_B': os.path.join(os.getcwd(), 'resources/images/choice/Hard_B.jpg'),
        'Resume_1': os.path.join(os.getcwd(), 'resources/images/choice/Resume_1.png'),
        'Resume_2': os.path.join(os.getcwd(), 'resources/images/choice/Resume_2.jpg'),
    },
    'end': {
        'gameover': os.path.join(os.getcwd(), 'resources/images/end/gameover.png'),
        'continue_red': os.path.join(os.getcwd(), 'resources/images/end/continue_red.png'),
        'continue_black': os.path.join(os.getcwd(), 'resources/images/end/continue_black.png'),
    },
    'game': {
        'arrow1': os.path.join(os.getcwd(), 'resources/images/game/arrow1.png'), 
        'arrow2': os.path.join(os.getcwd(), 'resources/images/game/arrow2.png'), 
        'arrow3': os.path.join(os.getcwd(), 'resources/images/game/arrow3.png'), 
        'basic_tower': os.path.join(os.getcwd(), 'resources/images/game/basic_tower.png'), 
        'boulder': os.path.join(os.getcwd(), 'resources/images/game/boulder.png'), 
        'bush': os.path.join(os.getcwd(), 'resources/images/game/bush.png'), 
        'cave': os.path.join(os.getcwd(), 'resources/images/game/cave.png'), 
        'dirt': os.path.join(os.getcwd(), 'resources/images/game/dirt.png'), 
        'enemy_blue': os.path.join(os.getcwd(), 'resources/images/game/enemy_blue.png'), 
        'enemy_pink': os.path.join(os.getcwd(), 'resources/images/game/enemy_pink.png'), 
        'enemy_red': os.path.join(os.getcwd(), 'resources/images/game/enemy_red.png'), 
        'enemy_yellow': os.path.join(os.getcwd(), 'resources/images/game/enemy_yellow.png'), 
        'godark': os.path.join(os.getcwd(), 'resources/images/game/godark.png'), 
        'golight': os.path.join(os.getcwd(), 'resources/images/game/golight.png'), 
        'grass': os.path.join(os.getcwd(), 'resources/images/game/grass.png'), 
        'grass_1': os.path.join(os.getcwd(), 'resources/images/game/spr_grass_01.png'), 
        'Ground_1': os.path.join(os.getcwd(), 'resources/images/game/spr_tile_set_ground.png'), 
        'healthfont': os.path.join(os.getcwd(), 'resources/images/game/healthfont.png'), 
        'heavy_tower': os.path.join(os.getcwd(), 'resources/images/game/heavy_tower.png'), 
        'med_tower': os.path.join(os.getcwd(), 'resources/images/game/med_tower.png'), 
        'nexus': os.path.join(os.getcwd(), 'resources/images/game/nexus.png'), 
        'othergrass': os.path.join(os.getcwd(), 'resources/images/game/othergrass.png'), 
        'path': os.path.join(os.getcwd(), 'resources/images/game/path.png'), 
        'rock': os.path.join(os.getcwd(), 'resources/images/game/rock.png'), 
        'tiles': os.path.join(os.getcwd(), 'resources/images/game/tiles.png'), 
        'unitfont': os.path.join(os.getcwd(), 'resources/images/game/unitfont.png'), 
        'water': os.path.join(os.getcwd(), 'resources/images/game/water.png'), 
        'x': os.path.join(os.getcwd(), 'resources/images/game/x.png'),
        'Castle_Easy': os.path.join(os.getcwd(), 'resources/images/game/spr_castle_green.png'), 
        'Castle_Mid': os.path.join(os.getcwd(), 'resources/images/game/spr_castle_blue.png'), 
        'Castle_Hard': os.path.join(os.getcwd(), 'resources/images/game/spr_castle_red.png'),
        'T1': os.path.join(os.getcwd(), 'resources/images/game/T1.png'), 
        'T2': os.path.join(os.getcwd(), 'resources/images/game/T2.png'), 
        'T3': os.path.join(os.getcwd(), 'resources/images/game/T3.png'), 
        'T4': os.path.join(os.getcwd(), 'resources/images/game/T4.png'), 
        'T5': os.path.join(os.getcwd(), 'resources/images/game/T5.png'),
        'T6': os.path.join(os.getcwd(), 'resources/images/game/T6.png'),    
        'arrow_1': os.path.join(os.getcwd(), 'resources/images/game/arrow_1.png'), 
        'arrow_2': os.path.join(os.getcwd(), 'resources/images/game/arrow_2.png'), 
        'arrow_3': os.path.join(os.getcwd(), 'resources/images/game/arrow_3.png'), 
        'arrow_4': os.path.join(os.getcwd(), 'resources/images/game/arrow_4.png'), 
        'arrow_5': os.path.join(os.getcwd(), 'resources/images/game/arrow_5.png'), 
        'arrow_6': os.path.join(os.getcwd(), 'resources/images/game/arrow_6.png'), 
        'enemy_1_1': os.path.join(os.getcwd(), 'resources/images/game/Monsters/spr_goblin_1.png'), 
        'enemy_1_2': os.path.join(os.getcwd(), 'resources/images/game/Monsters/spr_goblin_2.png'), 
        'enemy_1_3': os.path.join(os.getcwd(), 'resources/images/game/Monsters/spr_goblin_3.png'),
        'enemy_1_4': os.path.join(os.getcwd(), 'resources/images/game/Monsters/spr_goblin_4.png'), 
        'enemy_2_1': os.path.join(os.getcwd(), 'resources/images/game/Monsters/spr_zombie_1.png'), 
        'enemy_2_2': os.path.join(os.getcwd(), 'resources/images/game/Monsters/spr_zombie_2.png'), 
        'enemy_2_3': os.path.join(os.getcwd(), 'resources/images/game/Monsters/spr_zombie_3.png'), 
        'enemy_2_4': os.path.join(os.getcwd(), 'resources/images/game/Monsters/spr_zombie_4.png'), 
        'enemy_3_1': os.path.join(os.getcwd(), 'resources/images/game/Monsters/spr_bat_1.png'),
        'enemy_3_2': os.path.join(os.getcwd(), 'resources/images/game/Monsters/spr_bat_2.png'),  
        'enemy_3_3': os.path.join(os.getcwd(), 'resources/images/game/Monsters/spr_bat_3.png'),  
        'enemy_3_4': os.path.join(os.getcwd(), 'resources/images/game/Monsters/spr_bat_4.png'),  
        'enemy_4_1': os.path.join(os.getcwd(), 'resources/images/game/Monsters/spr_demon_1.png'),  
        'enemy_4_2': os.path.join(os.getcwd(), 'resources/images/game/Monsters/spr_demon_2.png'),  
        'enemy_4_3': os.path.join(os.getcwd(), 'resources/images/game/Monsters/spr_demon_3.png'),  
        'enemy_4_4': os.path.join(os.getcwd(), 'resources/images/game/Monsters/spr_demon_4.png'),
        'Bomb': os.path.join(os.getcwd(), 'resources/images/game/Bomb.png'),  
        'pause': os.path.join(os.getcwd(), 'resources/images/game/pause.png'),   
        
    },
    'pause': {
        'gamepaused': os.path.join(os.getcwd(), 'resources/images/pause/gamepaused.png'), 
        'resume_black': os.path.join(os.getcwd(), 'resources/images/pause/resume_black.png'), 
        'resume_red': os.path.join(os.getcwd(), 'resources/images/pause/resume_red.png'), 
    },
    'start': {
        'play_black': os.path.join(os.getcwd(), 'resources/images/start/play_black.png'), 
        'play_red': os.path.join(os.getcwd(), 'resources/images/start/play_red.png'), 
        'quit_black': os.path.join(os.getcwd(), 'resources/images/start/quit_black.png'), 
        'quit_red': os.path.join(os.getcwd(), 'resources/images/start/quit_red.png'), 
        'start_interface': os.path.join(os.getcwd(), 'resources/images/start/start_interface.png'), 
    },
}

MAPPATHS = {
    '1': os.path.join(os.getcwd(), 'resources/maps/1.map'),
    '2': os.path.join(os.getcwd(), 'resources/maps/2.map'),
    '3': os.path.join(os.getcwd(), 'resources/maps/3.map'),
}

FONTPATHS = {
    'Calibri': os.path.join(os.getcwd(), 'resources/fonts/Calibri.ttf'),
    'm04': os.path.join(os.getcwd(), 'resources/fonts/m04.ttf'),
    'Microsoft Sans Serif': os.path.join(os.getcwd(), 'resources/fonts/Microsoft Sans Serif.ttf'),
}

DIFFICULTYPATHS = {
    'easy': os.path.join(os.getcwd(), 'resources/difficulties/easy.json'),
    'hard': os.path.join(os.getcwd(), 'resources/difficulties/hard.json'),
    'medium': os.path.join(os.getcwd(), 'resources/difficulties/medium.json'),
}

AUDIOPATHS = {
    'bgm': os.path.join(os.getcwd(), 'resources/audios/bgm.mp3'),
}
nexus_positions = {
    "1.map": (1180, 700),
    "2.map": (100, 200),
    "3.map": (500, 300)
}