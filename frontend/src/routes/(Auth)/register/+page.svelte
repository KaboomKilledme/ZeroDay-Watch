<script>
    import Form from "$lib/Auth/Form/+page.svelte";
    const inputs = [
        {name:'username', placeholder:'Create Username', type:'text'},
        {name:'password', placeholder:'Create Password', type:'password'},
        {name:'checkPassword', placeholder:'Confirm Password', type:'password'},
    ]
    const btnText = "Sign Up"
</script>

<Form title="Register" inputs={inputs} btnText={btnText}/>