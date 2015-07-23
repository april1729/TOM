classdef Board
    %BOARD Summary of this class goes here
    %   Detailed explanation goes here
    
    properties
        
        boardMatrix
        
        mainBoardMatrix
        
        isGameOver
        
        whoseTurn
        
        lastBoard
    end
    
    
    
    
    
    methods
        function obj=makeMove(obj,player,subBoard,entry)
            obj=obj.setElement(subBoard,entry,player);
            r=(mod(subBoard-1,3))+1;
            c=(floor((subBoard-1)/3))+1;
            if obj.isWon(obj.getSubBoard(subBoard))
                obj.mainBoardMatrix(r,c)=player;
                if obj.isWon(obj.mainBoardMatrix)
                    fprintf('Player %f Wins!!!!!!',player)
                    
                    obj.isGameOver=1;
                end
            end
            
            obj.lastBoard=entry;
            if player==1
                obj.whoseTurn=2;
            else
                obj.whoseTurn=1;
            end
        end
        function b=isWon(obj,board)
            if obj.isAllSame(board(1,:))
                b=true;
            elseif obj.isAllSame(board(2,:))
                b=true;
            elseif obj.isAllSame(board(3,:))
                b=true;
            elseif obj.isAllSame(board(:,1))
                b=true;
            elseif obj.isAllSame(board(:,2))
                b=true;
            elseif obj.isAllSame(board(:,3))
                b=true;
            elseif obj.isAllSame([board(1,1),board(2,2),board(3,3)])
                b=true;
            elseif obj.isAllSame([board(1,3),board(2,2),board(3,1)])
                b=true;
            else
                b=false;
            end
            
        end
        
        function b=isAllSame(obj,a)
            if (a(1)==a(2)) & (a(2)==a(3) & a~=0)
                b=true;
            else
                b=false;
            end
        end
        
        function obj=makeBoard(obj)
            obj.boardMatrix=zeros(9);
            obj.mainBoardMatrix=zeros(3);
            obj.isGameOver=false;
            obj.lastBoard=5;
        end
        
        function sb=getSubBoard(obj,n)
            %n is number 1-9
            startRow=(mod(n-1,3))*3+1;
            startCol=(floor((n-1)/3))*3+1;
            
            sb=obj.boardMatrix(startRow:startRow+2,startCol:startCol+2);
        end
        
        function [r,c]=getIndex(obj,subBoard,entry)
            startRow=(mod(subBoard-1,3))*3+1;
            startCol=(floor((subBoard-1)/3))*3+1;
            
            row=mod(entry-1,3);
            col=floor((entry-1)/3);
            
            r=startRow+row;
            c=startCol+col;
        end
        
        function obj=setElement(obj,subBoard,entry,val)
            [r,c]=obj.getIndex(subBoard,entry);
            obj.boardMatrix(r,c)=val;
        end
        
        function val=getElement(obj,subBoard,entry)
            [r,c]=obj.getIndex(subBoard,entry);
            val=obj.boardMatrix(r,c);
        end
        
        function val=rateBoardOverallForPlayer(obj,player)
            sum=0;
            for i=1:9
                if obj.mainBoardMatrix(i)==0
                    sum=sum+obj.rateBoard(obj.getSubBoard(i),player);
                end
                
                if obj.mainBoardMatrix(i)==player
                    sum=sum+3;
                end
            end
            
            val=sum+18*obj.rateBoard(obj.mainBoardMatrix,player);
        end
        
        function val=rateBoard(obj,board,player)
            val=0;
            val=val+obj.isAlmostWon(board(1,:),player);
            val=val+obj.isAlmostWon(board(2,:),player);
            val=val+obj.isAlmostWon(board(3,:),player);
            val=val+obj.isAlmostWon(board(:,1),player);
            val=val+obj.isAlmostWon(board(:,2),player);
            val=val+obj.isAlmostWon(board(:,3),player);
            val=val+obj.isAlmostWon([board(1,1),board(2,2),board(3,3)],player);
            val=val+obj.isAlmostWon([board(1,3),board(2,2),board(3,1)],player);
            
            if val>0
                val=1;
            end
        end
        
        function b=isAlmostWon(obj,a,player)
            if sum(a==player)==2 &&sum(a==0)==1
                b=true;
            else
                b=false;
            end
        end
        
        
        function printBoard(obj)
            for i=1:9
                obj.printRow(i);
                if mod(i,3)==0 && i~=9
                    obj.printSpace();
                end
            end
        end
        function printRow(obj,i)
            row=obj.boardMatrix(i,:);
            
            for j=1:9
                fprintf(' %d ',row(j));
                if mod(j,3)==0 && j~=9
                    fprintf('  |  ');
                end
            end
            fprintf('\n');
        end
        
        
        function printSpace(obj)
            fprintf('_________________________________________ \n\n');
        end
    end
    
end

