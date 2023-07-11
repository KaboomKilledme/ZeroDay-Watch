<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\SourceController;
use App\Http\Controllers\BookmarkController;
use App\Http\Controllers\UserController;


/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

// Public Routes
Route::post('/login', [AuthController::class, 'login']);
Route::post('/register', [AuthController::class, 'register']);

Route::get('sources', [SourceController::class, 'getSources']);

Route::group(['middleware' => ['auth:sanctum']], function () {
    Route::apiResource('bookmarks', BookmarkController::class);
    Route::post('bookmarks/remove', [BookmarkController::class, 'deleteBookmark']);
    Route::post('users', [UserController::class, 'updateDetails']);
    Route::post('users/delete', [UserController::class, 'destroy']);
    Route::post ('/logout', [AuthController::class, 'logout']);
});

