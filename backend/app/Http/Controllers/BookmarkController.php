<?php

namespace App\Http\Controllers;
use Illuminate\Support\Facades\Auth;
use Illuminate\Http\Request;
use App\Traits\HttpResponse;
use App\Models\User;
use App\Models\Source;
use App\Models\SourceUser;
use App\Http\Requests\BookmarkRequest;
use App\Http\Resources\BookmarkResource;
use App\Http\Resources\SourceCollection;
use App\Http\Requests\RemoveBookmarkRequest;

class BookmarkController extends Controller
{
    use HttpResponse;


    public function index(Request $request){ // To get/filter bookmarked sources

        $user = User::where('id', Auth::user()->id)->first();

        $query = $request->all();
        $title = $query['title'];
        
        if($title !== NULL){ // If a users enters a search term

            // All sources a user has bookmarked id's
            $bookmarkedSources = SourceUser::where('user_id', $user->id)->pluck('source_id');

            // filtering for bookmarked sources, '%' means the term can be used in between any characters
            $sources = Source::whereIn('id', $bookmarkedSources)
            ->where('title', 'LIKE', '%' . $title . '%')->get();
        
            return new SourceCollection($sources);
        } 
            return new BookmarkResource($user->loadMissing('sources'));            
    }

    public function store(BookmarkRequest $request){ // To add a source to a user's bookmarks
        $request->validated($request->all());
        $sourcedId = $request->id;

        if(SourceUser::where('source_id', $sourcedId)->where('user_id', Auth::user()->id)->exists()){
            return $this->success('Source has been bookmarked');
        }

        $bookmarked = SourceUser::create([ // Adding row to pivot table
            'user_id' => Auth::user()->id,
            'source_id' => $sourcedId,
        ]);

        return $this->success('Source has been bookmarked');
    }

    public function deleteBookmark(RemoveBookmarkRequest $request){

        $sourceUser = SourceUser::where('source_id', $request->id)
        ->where('user_id', Auth::user()->id);
        
        if($sourceUser->exists()){
            $sourceUser->delete();
            return $this->success('Bookmark has been removed');
        }
      
    }
   
}
