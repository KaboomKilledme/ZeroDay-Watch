<script>
    import Searchbar from "$lib/Bookmarks/Searchbar/+page.svelte"
    import Sources from "$lib/Main/Sources/+page.svelte";
</script>

<div class="BookmarksSourcesContainer">
    <Searchbar />
    <Sources />
</div>

<style lang="scss">
    .BookmarksSourcesContainer{
        height: 100%;
        width: 100%;
        display: grid;
        display: -ms-grid;
        display: -moz-grid;
        grid-template-columns: repeat(20,1fr);
        grid-template-rows: repeat(20,1fr);
    }
</style>