<script>
    import Searchbar from "$lib/Bookmarks/Searchbar/+page.svelte"
    import Sources from "$lib/Main/Sources/+page.svelte";
    import Content from "$lib/Main/Content/+page.svelte";
    
    export let data;

    const isBookmark = true;
    let shownContent = null;
    let content;
    let sources = data.sources.data[0];

    function showContent(event){
        shownContent = event.detail.source.id
        if(shownContent !== null){
            content = event.detail.source
        }
    }

    function removeSave(event){
        
        sources = sources.filter(source => {
            return source.id !== event.detail.id
        })
    }

    function showSources(event){
        sources = event.detail.sources.data[0];
    }
        

</script>

<div class="BookmarksSourcesContainer">
    <Searchbar on:foundSources={showSources} authToken={data.authToken} />
    {#await sources}
        
    {:then sources}
        <Sources sources={sources}  on:showContent={showContent}/>
    {/await}
    
    {#if shownContent}
        <Content on:saved={removeSave} isBookmark={isBookmark} authToken={data.authToken} content={content} on:close={showContent} />
    {/if}
    
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