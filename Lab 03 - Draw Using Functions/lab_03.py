"""
This is lab_03.  My attempt to draw the starship Enterprise using functions.
"""

import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

def draw_saucer_shape():
    arcade.draw_circle_filled(210, 300, 200, (229, 228, 226))
    arcade.draw_arc_outline(210, 300, 100, 100, arcade.color.BLACK, 90, 270)

def draw_main_body():
    arcade.draw_lbwh_rectangle_filled(380, 265, 300, 70, (229, 228, 226))
    arcade.draw_arc_filled(680, 300, 30, 70, (207, 196, 207), -90, 90)

def draw_nacelle_spokes():
    arcade.draw_lbwh_rectangle_filled(570, 320, 30, 100, (229, 228, 226))
    arcade.draw_lbwh_rectangle_filled(570, 180, 30, 100, (229, 228, 226))

def draw_nacelles():
    arcade.draw_lbwh_rectangle_filled(470, 420, 480, 40, (229, 228, 226))
    arcade.draw_lbwh_rectangle_filled(470, 140, 480, 40, (228, 228, 226))
    arcade.draw_arc_filled(470, 440, 40, 40, arcade.color.RED, 90, 270)
    arcade.draw_arc_filled(470, 160, 40, 40, arcade.color.RED, 90, 270)
    arcade.draw_arc_filled(950, 440, 20, 40, (207, 196, 207), -90, 90)
    arcade.draw_arc_filled(950, 160, 20, 40, (207, 196, 207), -90, 90)
    arcade.draw_lbwh_rectangle_filled(920, 420, 30, 40, (207, 196, 207))
    arcade.draw_lbwh_rectangle_filled(920, 140, 30, 40, (207, 196, 207))

def draw_saucer_details():
    arcade.draw_circle_outline(210, 300, 200, arcade.color.BLACK)
    arcade.draw_circle_outline(210, 300, 175, arcade.color.BLACK)
    arcade.draw_line(210, 250, 310, 300, arcade.color.BLACK)
    arcade.draw_line(210, 350, 310, 300, arcade.color.BLACK)
    arcade.draw_circle_outline(210, 300, 20, arcade.color.BLACK)
    arcade.draw_text("U.S.S. ENTERPRISE", 130, 372, arcade.color.BLACK, 16, rotation=90)
    arcade.draw_text("N", 110, 400, arcade.color.BLACK, 30, rotation=135)
    arcade.draw_text("C", 85, 370, arcade.color.BLACK, 30, rotation=120)
    arcade.draw_text("C", 70, 335, arcade.color.BLACK, 30, rotation=105)
    arcade.draw_text("-", 65, 300, arcade.color.BLACK, 30, rotation=90)
    arcade.draw_text("1", 65, 275, arcade.color.BLACK, 30, rotation=79)
    arcade.draw_text("7", 70, 250, arcade.color.BLACK, 30, rotation=68)
    arcade.draw_text("0", 80, 225, arcade.color.BLACK, 30, rotation=57)
    arcade.draw_text("1", 95, 200, arcade.color.BLACK, 30, rotation=45)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Starship Enterprise")
    arcade.set_background_color(arcade.color.BLACK)

    arcade.start_render()

    draw_saucer_shape()
    draw_main_body()
    draw_nacelle_spokes()
    draw_nacelles()
    draw_saucer_details()

    arcade.finish_render()
    arcade.run()

# Call the main function to get the program started.
main()
