<script>
    import Options from "$lib/Settings/Options/+page.svelte";
    import UpdateForm from "$lib/Settings/UpdateForm/+page.svelte";
    import LogOutPrompt from "$lib/Settings/LogOutPrompt/+page.svelte";
    import DeleteAccountPrompt from "$lib/Settings/DeleteAccountPrompt/+page.svelte";

    let shownOption = null;

    function updateOption(event){
        shownOption = event.detail.id;
    }


</script>

<div class="SettingsContainer">
    {#if shownOption === 1}
        <UpdateForm on:close={updateOption}/>
    {:else if shownOption === 2}
        <LogOutPrompt on:close={updateOption} />
    {:else if shownOption === 3}
        <DeleteAccountPrompt on:close={updateOption} />
    {/if}
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