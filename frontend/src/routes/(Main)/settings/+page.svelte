<script>
    import Options from "$lib/Settings/Options/+page.svelte";
    import UpdateForm from "$lib/Settings/UpdateForm/+page.svelte";

    let shownOption = null;

    function updateOption(event){
        shownOption = event.detail.id;
        console.log(shownOption);
    }

    function closeOption(event){
        shownOption = event.detail.id;
    }

</script>

<div class="SettingsContainer">
    {#if shownOption === 1}
        <UpdateForm on:close={closeOption}/>
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