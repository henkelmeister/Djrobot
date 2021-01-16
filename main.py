
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    # Use a breakpoint in the code line below to debug your script.
    print('Hi')  # Press Ctrl+F8 to toggle the breakpoint.
    dj = DJ()
    test = Song(name='first to play', artist='artist name', length=252, sid='1')
    test2 = Song(name='adsadasd', artist='bla bla bla', length=2522, sid='12323132')
    test3 = Song(name='last', artist='camilo', length=2523, sid='3')
    test4 = Song(name='lastsong', artist='camilo', length=25234, sid='5')
    test5 = Song(name='lastsong', artist='camilo', length=25234, sid='5')
    dj.addSong(test)
    dj.addSong(test2)
    dj.addSong(test3)
    dj.addSong(test4)
    dj.addSong(test5)
    dj.printPlaylist()

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    from Song import Song
    import time
    from DJ import DJ
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
