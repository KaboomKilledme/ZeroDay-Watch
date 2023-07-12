<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Hash;
use App\Models\User;
use App\Models\SourceUser;
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
            $password = $request->password;
            $passwordLen = strlen($password);

            if($passwordLen < 8){
                return $this->error('', 'Password must have more than 7 characters', 422);
            }

            $password = Hash::make($password);
        }

        $user->update([
            "name" => $username,
            "password" => $password
        ]);

        return $this->success('Your details have been updated');

    }

    public function destroy(){
        
        $user = User::where('id', Auth::user()->id)->first();
        $bookmarkedSources = SourceUser::where('user_id', $user->id);

        Auth::user()->currentAccessToken()->delete(); 
        $bookmarkedSources->delete();
        $user->delete();

        return $this->success('Your Account has been deleted');
   
    }
}
