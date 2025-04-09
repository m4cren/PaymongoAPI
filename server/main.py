from backend import socketio, create_website




app = create_website()




if __name__ == "__main__":
    socketio.run(app, debug=True, host='192.168.1.33', port=8888)
