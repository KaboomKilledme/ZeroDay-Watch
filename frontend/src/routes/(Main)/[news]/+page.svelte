<script>
    import Sources from "$lib/Main/Sources/+page.svelte";
    import SourceSelector from "$lib/News/SourceSelector/+page.svelte";
    import Content from "$lib/Main/Content/+page.svelte";

    export let data;

    let shownContent = null;
    let content;

    function showContent(event){
        shownContent = event.detail.source.id
        if(shownContent !== null){
            content = event.detail.source
        }
    }

</script>


<div class="NewsSourcesContainer">
    <SourceSelector />

    {#await data}
        Loading...
    {:then data} 
        {#if data.sources}
            <Sources sources={data.sources}  on:showContent={showContent} />
        {/if}
    {/await}
    

    {#if shownContent}
        <Content content={content} authToken={data.authToken} on:close={showContent} />
    {/if}
</div>


<style lang="scss">
    .NewsSourcesContainer{
        height: 100%;
        width: 100%;
        display: grid;
        display: -ms-grid;
        display: -moz-grid;
        grid-template-columns: repeat(20,1fr);
        grid-template-rows: repeat(20,1fr);
    }
 
</style>