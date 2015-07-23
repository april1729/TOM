classdef Move
    %MOVE Summary of this class goes here
    %   Detailed explanation goes here
    
    properties
        board
        entry
        player
    end
    
    methods
        function m=Move(player,board,entry)
            m.board=board;
            m.entry=entry;
            m.player=player;
        end
    end
    
end

