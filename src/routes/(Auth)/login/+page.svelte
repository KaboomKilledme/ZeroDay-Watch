<script>
    import Form from "$lib/Auth/Form/+page.svelte";
    const inputs = [
        {name:'username', placeholder:'Enter Username', type:'text'},
        {name:'password', placeholder:'Enter Password', type:'password'},
    ]
    const btnText = "Sign In"
</script>

<Form title="Login" inputs={inputs} btnText={btnText}/>