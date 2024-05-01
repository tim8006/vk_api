from flask import Flask, render_template
from vk_api import VkApi

app = Flask(__name__)


def get_vk_stats(group_id):
    vk_session = VkApi()
    vk = vk_session.get_api()
    stats = vk.stats_get(group_id, fields='reach')
    return stats


@app.route('/vk_stat/<int:group_id>')
def vk_stat(group_id):
    stats = get_vk_stats(group_id)
    return render_template('stats_table.html', stats=stats)


if __name__ == '__main__':
    app.run()
