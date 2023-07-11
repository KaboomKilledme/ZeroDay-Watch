<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Hash;
use App\Models\User;
use App\Http\Requests\UpdateUserRequest;
use App\Traits\HttpResponse;

class UserController extends Controller
{
    use HttpResponse;

    public function updateDetails(UpdateUserRequest $request){
        $request->validated($request->all());

        $user = User::find(Auth::user()->id);

        $username = $user->name;
        $password = $user->password;

        if($request->name !== NULL){
            $username = $request->name;
        }
        if($request->password !== NULL){
            $password = Hash::make($request->password);
        }

        $user->update([
            "name" => $username,
            "password" => $password
        ]);

        return $this->success('Your details have been updated');

    }

    public function destroy(){
        
        $user = User::find(Auth::user()->id);
        Auth::user()->currentAccessToken()->delete(); 
        $user->delete();
        return $this->success('Your Account has been deleted');
   
    }
}
