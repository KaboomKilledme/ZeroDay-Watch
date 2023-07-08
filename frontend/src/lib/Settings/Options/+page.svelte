<script>
    import {createEventDispatcher} from "svelte";
    import Option from "$lib/Settings/Options/Option/+page.svelte"

    const dispatch = createEventDispatcher()

    let options = [
        {id:1, name:'Update Details', icon:'fa-pen-to-square', isDelete:false},
        {id:2, name:'Log Out', icon:'fa-solid fa-right-from-bracket', isDelete:false},
        {id:3, name:'Delete Account', icon:'fa-user-slash', isDelete:true}
    ]

    function showOption(event){
        dispatch('option', {
            id:event.detail.id
        })
    }
</script>

{#each options as option}
    <Option option={option} on:option={showOption} />
{/each}
