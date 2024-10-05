import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_lbwh_rectangle_outline(0, 0, 300, 300, arcade.color.BLACK)
    arcade.draw_lbwh_rectangle_outline(300, 0, 300, 300, arcade.color.BLACK)
    arcade.draw_lbwh_rectangle_outline(600, 0, 300, 300, arcade.color.BLACK)
    arcade.draw_lbwh_rectangle_outline(900, 0, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_lbwh_rectangle_outline(0, 300, 300, 300, arcade.color.BLACK)
    arcade.draw_lbwh_rectangle_outline(300, 300, 300, 300, arcade.color.BLACK)
    arcade.draw_lbwh_rectangle_outline(600, 300, 300, 300, arcade.color.BLACK)
    arcade.draw_lbwh_rectangle_outline(900, 300, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = column * 10 + 2.5 # Instead of zero, calculate the proper x location using 'column'
            y = row * 10 + 2.5 # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_lbwh_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    # Below, replace "pass" with your code for the loop.
    # Use the modulus operator and an if statement to select the color
    # Don't loop from 30 to 60 to shift everything over, just add 300 to x.
    for row in range(30):
        for column in range(30):
            x = column * 10 + 2.5  # Instead of zero, calculate the proper x location using 'column'
            y = row * 10 + 2.5  # Instead of zero, calculate the proper y location using 'row'
            if column % 2:
                arcade.draw_lbwh_rectangle_filled(300 + x, y, 5, 5, arcade.color.BLACK)
            else:
                arcade.draw_lbwh_rectangle_filled(300 + x, y, 5, 5, arcade.color.WHITE)


def draw_section_3():
    # Use the modulus operator and an if/else statement to select the color.
    # Don't use multiple 'if' statements.
    for row in range(30):
        for column in range(30):
            x = column * 10 + 2.5  # Instead of zero, calculate the proper x location using 'column'
            y = row * 10 + 2.5  # Instead of zero, calculate the proper y location using 'row'
            if row % 2:
                arcade.draw_lbwh_rectangle_filled(600 + x, y, 5, 5, arcade.color.BLACK)
            else:
                arcade.draw_lbwh_rectangle_filled(600 + x, y, 5, 5, arcade.color.WHITE)



def draw_section_4():
    # Use the modulus operator and just one 'if' statement to select the color.
    for row in range(30):
        for column in range(30):
            x = column * 10 + 2.5  # Instead of zero, calculate the proper x location using 'column'
            y = row * 10 + 2.5  # Instead of zero, calculate the proper y location using 'row'
            if row % 2 == 0 and column % 2 == 0:
                arcade.draw_lbwh_rectangle_filled(900 + x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_lbwh_rectangle_filled(900 + x, y, 5, 5, arcade.color.BLACK)



def draw_section_5():
    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.
    for row in range(30):
        for column in range(row + 1, 30):
            x = column * 10 + 2.5 # Instead of zero, calculate the proper x location using 'column'
            y = row * 10 + 2.5 # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_lbwh_rectangle_filled(x, 300 + y, 5, 5, arcade.color.WHITE)



def draw_section_6():
    for row in range(30):
        for column in range(30 - row):
            x = column * 10 + 2.5 # Instead of zero, calculate the proper x location using 'column'
            y = row * 10 + 2.5 # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_lbwh_rectangle_filled(300 + x, 300 + y, 5, 5, arcade.color.WHITE)



def draw_section_7():
    for row in range(30):
        for column in range(row + 1):
            x = column * 10 + 2.5 # Instead of zero, calculate the proper x location using 'column'
            y = row * 10 + 2.5 # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_lbwh_rectangle_filled(600 + x, 300 + y, 5, 5, arcade.color.WHITE)



def draw_section_8():
    for row in range(30):
        for column in range(row + 2):
            x = (30 - column) * 10 + 2.5 # Instead of zero, calculate the proper x location using 'column'
            y = row * 10 + 2.5 # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_lbwh_rectangle_filled(900 + x, 300 + y, 5, 5, arcade.color.WHITE)



def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()