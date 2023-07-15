<script>
    import SourceCard from "$lib/Main/Sources/SourceCard/+page.svelte";
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();

    function showContent(event){
        dispatch('showContent', {
            source:event.detail.source
        })
    }

    export let sources;

</script>

<div class="Sources">
    
    {#if sources.length === 0}
        <h1>No Sources Found</h1>
    {:else}
        {#each sources as source}
            <SourceCard on:showContent={showContent} source={source} />
        {/each}
    {/if}
    

</div>


<style lang="scss">
    h1{
        font-size: 2rem;
        color: white;
        font-family: $primaryFont;
    }
     .Sources{
            overflow-y: hidden;
            grid-column: 1/21;
            grid-row: 4/21;
            height: 100%;
            width:100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            overflow-x: scroll;
        }
</style>