/*
https://github.com/giraf-fe
*/

#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

struct MatrixCoordinate {
    enum SurrondingPositions {
        UP, UPLF, LF, DWNLF, DWN, DWNRT, RT, UPRT
    };
    unsigned int row, col;
    MatrixCoordinate(unsigned int row, unsigned int col) {
        this->row = row;
        this->col = col;
    }
    MatrixCoordinate() = default;

    MatrixCoordinate atOtherPosition(SurrondingPositions pos) {
        switch (pos)
        {
        case MatrixCoordinate::UP:
            return this->up();
            break;
        case MatrixCoordinate::UPLF:
            return this->upLf();
            break;
        case MatrixCoordinate::LF:
            return this->Lf();
            break;
        case MatrixCoordinate::DWNLF:
            return this->dwnLf();
            break;
        case MatrixCoordinate::DWN:
            return this->dwn();
            break;
        case MatrixCoordinate::DWNRT:
            return this->dwnRt();
            break;
        case MatrixCoordinate::RT:
            return this->Rt();
            break;
        case MatrixCoordinate::UPRT:
            return this->upRt();
            break;
        default:
            return *this;
            break;
        }
    }

    MatrixCoordinate up() { return MatrixCoordinate(this->row - 1, this->col); }
    MatrixCoordinate upLf() { return MatrixCoordinate(this->row - 1, this->col - 1); }
    MatrixCoordinate Lf() { return MatrixCoordinate(this->row, this->col - 1); }
    MatrixCoordinate dwnLf() { return MatrixCoordinate(this->row + 1, this->col - 1); }
    MatrixCoordinate dwn() { return MatrixCoordinate(this->row + 1, this->col); }
    MatrixCoordinate dwnRt() { return MatrixCoordinate(this->row + 1, this->col + 1); }
    MatrixCoordinate Rt() { return MatrixCoordinate(this->row, this->col + 1); }
    MatrixCoordinate upRt() { return MatrixCoordinate(this->row - 1, this->col + 1); }

    bool operator==(const MatrixCoordinate& other) const {
        return this->row == other.row && this->col == other.col;
    }

};

struct NumberMatrix {
    unsigned int* matrixdata;
    unsigned int rows, cols;

    NumberMatrix(unsigned int rows, unsigned int cols) {
        this->rows = rows;
        this->cols = cols;
        this->matrixdata = new unsigned int[rows * cols];
    }
    bool getPos(const MatrixCoordinate& coord, unsigned int* val) const {
        if (coord.col >= this->cols || coord.row >= this->rows) {
            return false;
        }
        *val = this->matrixdata[coord.row * this->cols + coord.col];
        return true;
    }
    void setPos(const MatrixCoordinate& coord, unsigned int val) {
        this->matrixdata[coord.row * this->cols + coord.col] = val;
    }
};

struct PathNode {
    PathNode* previousNode;
    MatrixCoordinate currentPosition;
    std::vector<PathNode*> nextPositions;
    PathNode(const MatrixCoordinate& c, PathNode* prevnode) {
        this->currentPosition = c;
        this->previousNode = prevnode;
    }
    void freeNodes() {
        for (PathNode* p : this->nextPositions) {
            p->freeNodes();
            delete p;
        }
    }
};

void traverseNextPathsRecursive(const NumberMatrix& board, PathNode* node, std::vector<PathNode*>& prohibitedNodes) {
    //step 1: get the 2 search values
    unsigned int sc_a; board.getPos(node->currentPosition, &sc_a);
    unsigned int sc_b = sc_a * 2;

    

    //step 2: search in all 8 directions
    for (int i = 0; i < 8; i++) {
        unsigned int val;
        MatrixCoordinate otherpos = node->currentPosition.atOtherPosition((MatrixCoordinate::SurrondingPositions)i);
        bool skip = false;
        for (PathNode* pnodes : prohibitedNodes) {
            if (otherpos == pnodes->currentPosition) {
                //skip
                skip = true;
                break;
            }
        }
        if (skip) continue;
        if (board.getPos(otherpos, &val)) {
            if (val == sc_a || val == sc_b) {
                node->nextPositions.push_back(new PathNode(otherpos, node));
            }
        }
    }

    //step 3: traverse next paths
    for (PathNode* pn : node->nextPositions) {
        prohibitedNodes.push_back(pn);
        traverseNextPathsRecursive(board, pn, prohibitedNodes);
        prohibitedNodes.pop_back();
    }
}

std::string stringifyPath(std::vector<PathNode*> path) {
    std::string str;
    for (int i = 0; i < path.size(); i++) {
        str += std::to_string(path[i]->currentPosition.row + 1); //strings are one based indexing
        str += std::to_string(path[i]->currentPosition.col + 1);
    }
    return str;
}

void buildPathsRecursive(std::vector<PathNode*>& currentPath, std::vector<PathNode*>& longestPath, PathNode* node) {
    if (node->nextPositions.empty()) {
        if (currentPath.size() > longestPath.size()) {
            longestPath = currentPath;
        }
        else if (currentPath.size() == longestPath.size()) {
            //do the string thing
            std::string current = stringifyPath(currentPath);
            std::string longest = stringifyPath(longestPath);
            int rc = std::memcmp(current.c_str(), longest.c_str(), current.size());
            if (rc < 0) longestPath = currentPath;
        }
    }
    else {
        for (PathNode* pn : node->nextPositions) {
            currentPath.push_back(pn);
            buildPathsRecursive(currentPath, longestPath, pn);
            currentPath.pop_back();
        }
    }
}

void traversePaths(const NumberMatrix& board, PathNode* rootNode, std::vector<PathNode*>& lngstPth) {
    //step 1: look at cells in all 8 directions, check if they have same value
    unsigned int currentNodeVal; board.getPos(rootNode->currentPosition, &currentNodeVal);

    
    for (int i = 0; i < 8; i++) {
        unsigned int val;
        MatrixCoordinate otherpos = rootNode->currentPosition.atOtherPosition((MatrixCoordinate::SurrondingPositions)i);
        if (board.getPos(otherpos, &val)) {
            if (val == currentNodeVal) {
                rootNode->nextPositions.push_back(new PathNode(otherpos, rootNode));
            }
        }
    }

    //step 2: traverse next paths
    std::vector<PathNode*> prohibitedNodes;
    prohibitedNodes.push_back(rootNode);
    for (PathNode* pn : rootNode->nextPositions) {
        prohibitedNodes.push_back(pn);
        traverseNextPathsRecursive(board, pn, prohibitedNodes);
        prohibitedNodes.pop_back();
    }

    //step 3: branch out from root node and find longest path
    std::vector<PathNode*> currentPath;
    currentPath.push_back(rootNode); //gotta initiate the path
    std::vector<PathNode*> longestPath;
    buildPathsRecursive(currentPath, longestPath, rootNode);

    //step 4: compare to current longest path
    if (longestPath.size() > lngstPth.size()) {
        bool freeable = !lngstPth.empty();
        if (freeable) {
            PathNode* oldRootNode = lngstPth[0];
            lngstPth = longestPath;
            oldRootNode->freeNodes();
            delete oldRootNode;
        }
        else {
            lngstPth = longestPath;
        }
    }
    else if (longestPath.size() == lngstPth.size()) {
        //do the string thing
        std::string current = stringifyPath(longestPath);
        std::string longest = stringifyPath(lngstPth);
        int rc = std::memcmp(current.c_str(), longest.c_str(), current.size());
        if (rc < 0) {
            bool freeable = !lngstPth.empty();
            if (freeable) {
                PathNode* oldRootNode = lngstPth[0];
                lngstPth = longestPath;
                oldRootNode->freeNodes();
                delete oldRootNode;
            }
            else {
                lngstPth = longestPath;
            }
        }
    }
    else {
        longestPath[0]->freeNodes();
    }
}
int nextPowerOfTwo(int n) {
    if (n == 0) return 1;
    n--;

    n |= n >> 1;
    n |= n >> 2;
    n |= n >> 4;
    n |= n >> 8;
    n |= n >> 16;

    return n + 1;
}

std::string play2248(const std::string& boardValues) {

    //step 1: build array structure
    NumberMatrix board(8, 5);

    //step 2: fill
    {
        std::vector<unsigned int> nums;
        const char* boardstr = boardValues.c_str();
        //read until [spc] or string end
        std::string numstr;
        unsigned int idx = 0;
        while (true)
        {
            if (boardstr[idx] == ' ') {

                nums.push_back(std::stoi(numstr));
                numstr = "";
                idx++;
                continue;
            }
            if (boardstr[idx] == '\0') {
                nums.push_back(std::stoi(numstr));
                break;
            }
            numstr += boardstr[idx];
            idx++;
        }

        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 5; j++) {
                board.setPos(MatrixCoordinate(i, j), nums.at(i * 5 + j));
            }
        }
    }

    for (int r = 0; r < 3; r++) {
        //step 3: for each cell, look for longest path
        std::vector<PathNode*> longestPath;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 5; j++) {
                PathNode* rootnode = new PathNode(MatrixCoordinate(i, j), nullptr);
                traversePaths(board, rootnode, longestPath);
            }
        }


        //step 4: sum the path
        int sum = 0;
        for (PathNode* n : longestPath) {
            unsigned int a; board.getPos(n->currentPosition, &a);
            sum += a;
        }
        //find smallest power of 2 after sum
        int newPowerof2 = nextPowerOfTwo(sum);
        board.setPos(longestPath[longestPath.size() - 1]->currentPosition, newPowerof2);

        //step 5: find the smallest allowed number

        //we need the largest number present in the board
        unsigned int largest = board.matrixdata[0];
        for (int i = 1; i < 40; i++) {
            if (board.matrixdata[i] > largest) largest = board.matrixdata[i];
        }


        unsigned int smallestAllowedNumber = std::max(256u, largest) / 128;

        //step 6: remove values in the path + smaller than the smallest allowed number
        //set them to zero
        for (int i = 0; i < longestPath.size() - 1; i++) {
            board.setPos(longestPath[i]->currentPosition, 0);
        }

        //we dont need the nodes anymore after this point, free the nodes
        longestPath[0]->freeNodes();
        delete longestPath[0];

        for (int i = 0; i < 40; i++) {
            if (board.matrixdata[i] < smallestAllowedNumber) board.matrixdata[i] = 0;
        }

        //step 7: perform gravity
        //for every column
        for (int i = 0; i < 5; i++) {
            int writeIndex = 7;
            for (int j = 7; j >= 0; j--) {
                unsigned int val; board.getPos(MatrixCoordinate(j, i), &val);
                if (val != 0) {
                    unsigned int n; board.getPos(MatrixCoordinate(j, i), &n);
                    board.setPos(MatrixCoordinate(writeIndex--, i), n);
                    //board.setPos(MatrixCoordinate(j, i), 0);
                }
            }
            //writeindex + 1 == number of zeros to fill
            for (int j = 0; j < writeIndex + 1; j++) {
                board.setPos(MatrixCoordinate(j, i), 0);
            }
        }

        //step 8: fill empty spots
        //make array of valid numbers
        unsigned int validNumbers[8];
        validNumbers[0] = std::max(256u, largest);
        for (int i = 1; i < 8; i++) {
            validNumbers[i] = validNumbers[i - 1] / 2;
        }

        unsigned int fillCounter = 0;
        for (int i = 0; i < 40; i++) {
            if (board.matrixdata[i] == 0) {
                board.matrixdata[i] = validNumbers[fillCounter];
                fillCounter++;
                fillCounter %= 8;
            }
        }
    }
    //step 9: repeat 2 more times

    //step 10: convert board into a string
    std::string resultString;
    for (int i = 0; i < 40; i++) {
        resultString += std::to_string(board.matrixdata[i]);
        resultString += " ";
    }
    resultString.erase(resultString.begin() + resultString.size() - 1);

    return resultString;
}

void testoutput(const std::string& testcase, const std::string& actual, int num) {
    if (testcase != actual) {
        std::cout << "Failed test case " << num << std::endl << "Received output of " << actual << std::endl;
    }
    else {
        std::cout << "Passed test case " << num << std::endl;
    }
}

int main()
{

    testoutput(
        "4096 2048 1024 512 256 4096 128 64 32 4096 32 2048 1024 512 256 512 128 64 32 4096 32 2048 1024 256 512 256 256 256 256 64 32 128 64 256 1024 1024 128 256 64 32",
        play2248("4 128 4 128 32 16 16 4 256 16 32 4 16 64 4 8 64 64 256 8 16 2 2 256 4 32 128 2 64 8 256 32 128 16 2 8 32 32 4 32"), 1
    );
    testoutput(
        "4096 4096 2048 1024 256 4096 512 256 128 4096 32 64 32 4096 256 512 2048 1024 2048 4096 32 128 64 512 512 4096 2048 1024 32 64 32 128 64 512 1024 1024 2048 1024 32 32",
        play2248("256 128 64 128 32 32 16 8 256 16 4 2 16 64 4 4 128 64 256 8 16 16 2 256 4 32 64 2 64 8 256 2 128 16 2 8 128 256 4 32"), 2
    );
    testoutput(
        "8192 4096 2048 1024 512 256 128 64 8192 4096 2048 1024 512 256 128 1024 2048 1024 512 64 256 128 64 128 256 2048 8192 256 1024 64 64 512 64 1024 512 256 128 128 1024 256",
        play2248("256 16 256 2 32 2 16 2 16 8 32 2 256 64 16 4 2 128 2 32 8 8 32 256 2 2 4 8 32 128 16 16 32 64 256 4 16 128 4 8"), 3
    );
    testoutput(
        "2048 1024 512 256 128 64 32 16 2048 1024 512 512 256 128 64 32 256 32 16 2048 256 16 1024 512 256 64 2048 128 64 128 64 512 128 16 64 128 128 128 64 32",
        play2248("256 8 4 16 128 64 4 32 256 256 8 32 8 4 2 64 128 8 2 8 64 16 64 16 128 4 4 4 4 64 64 2 8 8 32 128 128 128 64 4"), 4
    );
    testoutput(
        "1024 512 256 128 64 64 32 16 128 512 1024 8 1024 1024 32 32 512 256 64 1024 256 16 8 8 32 128 256 128 64 32 128 128 128 1024 256 32 64 16 32 128",
        play2248("4 16 8 2 32 2 2 8 32 4 2 16 16 4 128 128 8 4 2 128 128 64 8 128 128 4 2 16 32 16 8 8 128 16 32 32 8 128 2 128"), 5
    );
}