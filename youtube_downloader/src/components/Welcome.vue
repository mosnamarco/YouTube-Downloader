<script>
export default {
    data() {
        return {
            counter: 0,
            word: '',
            listOfWords: ['Adds', 'Pop-Ups', 'Bullshit']
        }
    },
    mounted() {
        window.setInterval(() => {
            this.word = this.listOfWords[this.counter]
            if (this.counter < 2)
                this.counter++
            else
                this.counter = 0
        }, 2000)
    }
}

</script>

<template>
    <h1>Free Youtube Downloader</h1>
    <p><strong>No</strong> <span>{{ word }}</span> just pure download.</p>
    <!-- TODO: DONATION BUTTON (Probably Kofi) -->
    <span>Support me</span>
</template>

<style scoped>
</style>