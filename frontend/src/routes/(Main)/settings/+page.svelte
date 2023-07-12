<script>
    import Options from "$lib/Settings/Options/+page.svelte";
    import UpdateForm from "$lib/Settings/UpdateForm/+page.svelte";
    import LogOutPrompt from "$lib/Settings/LogOutPrompt/+page.svelte";
    import DeleteAccountPrompt from "$lib/Settings/DeleteAccountPrompt/+page.svelte";

    let shownOption = null;

    export let data;

    function updateOption(event){
        shownOption = event.detail.id;
    }


</script>

<div class="SettingsContainer">
    {#await data }
        
    {:then data } 
        {#if shownOption === 1}
            <UpdateForm authToken={data.authToken} on:close={updateOption}/>
        {:else if shownOption === 2}
            <LogOutPrompt authToken={data.authToken} on:close={updateOption} />
        {:else if shownOption === 3}
            <DeleteAccountPrompt authToken={data.authToken} on:close={updateOption} />
        {/if}
    {/await}
    
    <Options on:option={updateOption} />
</div>


<style lang="scss">
    .SettingsContainer{
        width: 100%;
        height: 100%;
        display: flex;
        display: -ms-flexbox;
        display: -webkit-flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
</style>