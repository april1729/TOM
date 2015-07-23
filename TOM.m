function TOM(difficulty)

b=Board;
b=b.makeBoard();

b.lastBoard=5;

disp('I am player 1, you are player 2.')
b.whoseTurn=input('who goes first?');

while ~b.isGameOver
    
    if b.whoseTurn==1
        b=makeMove(b);
    elseif b.whoseTurn==2
        b.printBoard()
        fprintf('\n\nMy score is: %d\nYour Score is: %d\n',b.rateBoardOverallForPlayer(1),b.rateBoardOverallForPlayer(2));

        b=promptMove(b);
    end
    
    
end


    function b=promptMove(b)
        board=input('What board are you playing in? (1-9)  ');
        entry=input('Where on the board will you play? (1-9)  ');
        b=b.makeMove(2,board,entry);

        
    end

    function b=makeMove(b)
        moves=getAllMoves(b);
        bestMove=moves(1);
        val=-inf;
        for move=moves
            newVal=minimax(move,b,difficulty,true);
            if newVal>val
                val=newVal;
                bestMove=move;
            end
        end
        
        %         for i=1:length(moves)
        %             move=moves(i);
        %             fprintf('%f: board %f, entry %f \n',i,move.board,move.entry)
        %         end
        %         i=input('what move should i make?  ');
        %        move=moves(i);
        
        
        b=b.makeMove(1,bestMove.board, bestMove.entry);

        
    end

    function moves=getAllMoves(b)
        moves=[];
        if b.mainBoardMatrix(b.lastBoard)==0
            for i=1:9
                if b.getElement(b.lastBoard,i)==0
                    moves=[moves,Move(b.whoseTurn,b.lastBoard,i)];
                end
            end
        else
            for board=1:9
                if b.mainBoardMatrix(board)==0
                    for i=1:9
                        if b.getElement(board,i)==0
                            moves=[moves,Move(b.whoseTurn,board,i)];
                        end
                    end
                end
            end
        end
    end

    function bestValue=minimax(node,board, depth, maximizingPlayer)
        board=board.makeMove(node.player,node.board,node.entry);
        if ((depth == 0))
            bestValue=board.rateBoardOverallForPlayer(1)-board.rateBoardOverallForPlayer(2);
            return
        end
        if board.isGameOver
            if maximizingPlayer
                bestValue=inf;
            else
                bestValue=-inf;
            end
            return
        end
                
        if (maximizingPlayer)
            bestValue = -inf;
            for child=getAllMoves(board)
                val = minimax(child, board,depth - 1, false);
                bestValue= max(bestValue, val);
            end
            return
        else
            bestValue = inf;
            for child=getAllMoves(board)
                val= minimax(child, board,depth - 1, true);
                bestValue = min(bestValue, val);
            end
            return
        end
    end        
end






