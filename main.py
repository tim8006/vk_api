import vk_api


def upload_photos():
    vk_session = vk_api.VkApi('<login>', '<password>')
    vk_session.auth()

    vk = vk_session.get_api()

    album_id = < album_id >
    group_id = < group_id >

    photos_path = 'static/img/'

    photo_files = ['photo1.jpg', 'photo2.jpg', 'photo3.jpg']

    for photo_file in photo_files:
        photo = photos_path + photo_file
        upload_url = vk.photos.getUploadServer(album_id=album_id, group_id=group_id)['upload_url']
        response = vk.http.post(upload_url, files={'file1': open(photo, 'rb')}).json()
        photo_info = vk.photos.save(album_id=album_id, group_id=group_id, server=response['server'],
                                    photos_list=response['photos_list'], hash=response['hash'])[0]

        vk.photos.addToAlbum(owner_id=-group_id, photo_id=photo_info['id'], album_id=album_id)

    print('Photos uploaded successfully!')


upload_photos()