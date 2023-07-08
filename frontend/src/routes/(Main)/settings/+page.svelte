<script>
    import Option from "$lib/Settings/Option/+page.svelte";

</script>

<div class="SettingsContainer">
    <Option name={'Update Details'} icon={"fa-pen-to-square"}/>
    <Option name={"Log Out"} icon={"fa-solid fa-right-from-bracket"} />
    <Option name={'Delete Account'} icon={"fa-user-slash"} isDelete={true}/>

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