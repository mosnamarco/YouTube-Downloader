<script setup>
import { ref } from 'vue';
import axios from 'axios'

const youtube_link = ref('')

// TODO Fix bugs
async function processDownload(youtube_link) {
    await axios('http://127.0.0.1:5000/download/?url=' + youtube_link.youtube_link)
}
</script>

<template>
    <div class="download_container">
        <div class="link_group_wrapper">
            <label for="youtube_url">Insert Link</label>
            <input name="youtube_url" type="url" placeholder="https://youtube.com/paste_your_link_here"
                v-model="youtube_link">
            <button @click="processDownload({ youtube_link })">Download Now</button>
        </div>

        <!-- TODO: make this so that it only shows after link has been processed -->
        <div class="preview_window">
            <!-- TODO: make it display thumbnail -->
            <img src="https://picsum.photos/300/200" alt="">
        </div>
        <div class="download_options_container">
            <!-- TODO: Provide Options (MP4, MP3) -->
            <div class="choice_mp4 choice">
                <span>MP4 [ Some Random Image.mp4 ] </span>
                <button>Download</button>
            </div>
            <div class="choice_mp3 choice">
                <span>MP3 [ Some Random Image.mp3 ] </span>
                <button>Download</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
.download_container {
    background-color: aliceblue;
    padding: 20px;
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    gap: 50px;
}

.download_options_container {
    color: black;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;
}

.link_group_wrapper {
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 20px;
    color: black;
}

label {
    position: absolute;
    top: -10px;
    left: 10px;
    background-color: aliceblue;
    padding-inline: 5px;
}

button {
    cursor: pointer;
    height: 50px;
    padding-inline: 25px;
    background-color: rgb(112, 214, 112);
    color: white;
    font-size: large;
    font-weight: bold;
    border: none;
    border-radius: 10px;
}

button:hover {
    background-color: rgb(75, 148, 75);
}

input {
    padding: 10px;
}

.choice {
    display: flex;
    align-items: center;
    align-content: center;
    gap: 20px;
}

.preview_window {
    margin: auto;
}
</style>